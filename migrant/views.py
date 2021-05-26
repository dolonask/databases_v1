from django.shortcuts import render, redirect

from .forms import CaseForm, CompanyForm, IndividualForm, VictimForm, GroupForm, EntrepreneurForm, PhotoForm, FileForm
from .filters import MigrantFilter

# Create your views here.
from .models import Case, CasePhoto, CaseFile


def append_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        victimForm = VictimForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)
        photoForm = PhotoForm(request.POST, request.FILES)
        fileForm = FileForm(request.POST, request.FILES)

        if form.is_valid():

            # cleaned_data = form.cleaned_data;
            form = form.save(commit=False)
            # if cleaned_data['source']:
            #     for item in cleaned_data['source']:
            #         if item.id == 5:
            #             pass
            if companyForm.is_valid():
                form.company = companyForm.save()

            if individualForm.is_valid():
                form.individualInfo = individualForm.save()
            if victimForm.is_valid():
                form.victim = victimForm.save()
            if groupForm.is_valid():
                form.personGroupInfo = groupForm.save()
            if entrepreneurForm.is_valid():
                form.entrepreneur = entrepreneurForm.save()


            form.user = request.user
            form.save()

            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CasePhoto(photo=f,card = form)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CaseFile(file=f,card=form)
                    file.save()

            return redirect('migrant_case')

    else:
        form = CaseForm
        companyForm = CompanyForm
        individualForm = IndividualForm
        victimForm = VictimForm
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
                      'victimForm': victimForm,
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                      'photoForm': photoForm,
                      'fileForm': fileForm,
                  })

def cases(request):

    cases = Case.objects.all().filter(user=request.user)

    filter = MigrantFilter(request.GET,queryset=cases)
    cards = filter.qs

    context = {'cards':cards, 'myFilter':filter}

    return render(request, 'migrant/cases.html', context)


def multistep(request):
    return render(request, 'migrant/add_case.html')