from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import CaseForm, CompanyForm, IndividualForm, GroupForm, EntrepreneurForm, PhotoForm, FileForm, CaseCommentForm
from .filters import MigrantFilter

# Create your views here.
from .models import *


@login_required
def append_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)
        photoForm = PhotoForm(request.POST, request.FILES)
        fileForm = FileForm(request.POST, request.FILES)

        if form.is_valid():

            # cleaned_data = form.cleaned_data;
            # if request.user.is_authenticated():
            #     form.instance.user = request.user
            # if cleaned_data['source']:
            #     for item in cleaned_data['source']:
            #         if item.id == 5:
            #             pass
            case = form.save(commit=False)


            if companyForm.is_valid():
                case.company = companyForm.save()
            if individualForm.is_valid():
                case.individualInfo = individualForm.save()
            # if victimForm.is_valid():
            #     victim = victimForm.save(commit=False)
            #     case.victim = victim
            #     victim.save()
            if groupForm.is_valid():
                case.personGroupInfo = groupForm.save()
            if entrepreneurForm.is_valid():
                case.entrepreneur = entrepreneurForm.save()

            case.user = request.user
            case.save()
            form.save_m2m()

            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CasePhoto(photo=f, card=case)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CaseFile(file=f, card=case)
                    file.save()

            return redirect('migrant_case')

    else:
        form = CaseForm
        companyForm = CompanyForm
        individualForm = IndividualForm
        groupForm = GroupForm
        entrepreneurForm = EntrepreneurForm
        photoForm = PhotoForm
        fileForm = FileForm

    return render(request,
                  'migrant/add_case.html',
                  context={
                      'form': form,
                      'companyForm': companyForm,
                      'individualForm': individualForm,
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                      'photoForm': photoForm,
                      'fileForm': fileForm,
                  })
@login_required()
def delete_case(request, pk):
    case = Case.objects.get(id=pk)
    case.active = False
    case.save()
    cases = Case.objects.filter(user=request.user, active = True)

    filter = MigrantFilter(request.GET,queryset=cases)
    cards = filter.qs

    context = {'cards':cards, 'myFilter':filter}

    return render(request, 'migrant/cases.html', context)

@login_required()
def update_case(request,pk):
    case = Case.objects.get(id=pk)

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)
        photoForm = PhotoForm(request.POST, request.FILES)
        fileForm = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)

        if companyForm.is_valid():
            case.company = companyForm.save()
        if individualForm.is_valid():
            case.individualInfo = individualForm.save()
        if groupForm.is_valid():
            case.personGroupInfo = groupForm.save()
        if entrepreneurForm.is_valid():
            case.entrepreneur = entrepreneurForm.save()

        case.user = request.user
        case.save()
        form.save_m2m()

        if photoForm.is_valid():
            for f in request.FILES.getlist('photo'):
                photo = CasePhoto(photo=f, card=case)
                photo.save()
        if fileForm.is_valid():
            for f in request.FILES.getlist('file'):
                file = CaseFile(file=f, card=case)
                file.save()

        return redirect('migrants_list')
    else:
        form = CaseForm(instance=case)

        companyForm = CompanyForm()
        if case.company is not None:
            companyForm = CompanyForm(instance=Company.objects.get(id=case.company))

        individualForm = IndividualForm
        if case.individualInfo is not None:
            individualForm = IndividualForm(instance=IndividualInfo.objects.get(id = case.individualInfo_id))

        # victimForm = VictimForm
        # if case.victim is not None:
        #     victimForm = VictimForm(instance=Victim.objects.get(id=case.victim_id))

        groupForm = GroupForm()
        if case.personGroupInfo is not None:
            groupForm = GroupForm(instance=PersonGroup.objects.get(id = case.personGroupInfo_id))

        entrepreneurForm = EntrepreneurForm
        if case.entrepreneur is not None:
            entrepreneurForm = EntrepreneurForm(instance = Entrepreneur.objects.get(id = case.entrepreneur_id))
        #
        # photos = CasePhoto.objects.get(card = case.id)
        # print(photos)
        photoForm = PhotoForm
        fileForm = FileForm

    return render(request,
                  'migrant/add_case.html',
                  context={
                      'form': form,
                      'companyForm': companyForm,
                      'individualForm': individualForm,
                      # 'victimForm': victimForm,
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                      'photoForm': photoForm,
                      'fileForm': fileForm,
                  })

def cases(request):

    cases = Case.objects.filter(user=request.user, active = True)

    filter = MigrantFilter(request.GET,queryset=cases)
    cards = filter.qs

    context = {'cards':cards, 'myFilter':filter}

    return render(request, 'migrant/cases.html', context)



def multistep(request):
    return render(request, 'migrant/add_case.html')


def download(request, case_id):
    pass


def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id)
    return render(request,'migrant/region_dropdown.html',{'regions':regions})


def add_comment(request, pk):
    case = Case.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data['case'] = case.id
        form = CaseCommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('migrants_list')
    else:
        form = CaseCommentForm()
    return render(request, 'migrant/add_comment.html', {'form': form, 'case': case})


def show_comments(request, pk):
    comments = CaseComment.objects.filter(case_id=pk, active=True)
    return render(request, 'migrant/show_comments.html', {'comments': comments})


def delete_comment(request, pk):
    case_comment = CaseComment.objects.get(id=pk)
    case_comment.active = False
    case_comment.save()
    return redirect('migrant_case_show_comments', case_comment.case_id)
