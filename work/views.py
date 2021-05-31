from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .filters import WorkFilter
from .forms import CaseForm, IndividualForm, PersonGroupForm, TradeUnionInfoForm, CompanyInfoForm, CasePhotoForm, \
    CaseFileForm
from .models import *

# Create your views here.

general_tabs_fields = [
    'case_name',
    'source',
    'source_another',
    'source_url',
    'source_content',
    'country',
    'region',
    'city_name',
    'case_company_name',
    'groupOfRights',
    'tradeUnionRight',
    'tradeUnionRightAnother',
    'tradeUnionCrime',
    'tradeUnionCrimeAnother',
    'meetingsRight',
    'meetingsRightAnother',
    'сonvention87',
    'сonvention98',
    'conversationRight',
    'conversationRightAnother',
    'principleOfNonDiscrimination',
    'discriminationInVariousAreas',
    'discriminationInVariousAreasAnother',
    'tradeUnionBuildingsRight',
    'tradeUnionBuildingsRightAnother',
    'createOrganizationRight',
    'createOrganizationRightAnother',
    'createTradeUnionRight',
    'createTradeUnionRightAnother',
    'electionsRight',
    'electionsRightAnother',
    'tradeUnionActivityRight',
    'tradeUnionActivityRightAnother',
    'createStrikeRight',
    'createStrikeRightAnother',
    'antiTradeUnionDiscrimination',
    'antiTradeUnionDiscriminationAnother',
    'сonvention135',
    'сonvention135Another',
    'consultationRight',
    'consultationRightAnother',
    'discriminatiOnVariousGrounds',
    'publicPolicyDiscrimination',
    'childLabor',
    'сonvention138',
    'convention182',
    'prohibitionOfForcedLabor',
    'useOfForcedLabor',
    'governmentCoercion',
    'violationsUsingCompulsoryLabor',
    'failureSystemicMeasures',
    'start_date',
    'end_date',
]
initiator_tab_fields = [
    'victim'
]
intruder_tab_fields = [
    'intruder',
    'intruderAnother',
    'government_agency_name',
    'local_agency_name',
    'police_agency_name',
    # 'control_agency_name',
]
description_tab_fields = [
    'exact_data',
    'case_description',
    'actions',
    'result',
    'violation_nature',
    'rights_state',
    'rights_state_another',
    'victim_situation',
    'victim_situation_another',
    'tradeUnionSituation',
    'tradeUnionSituation_another',
    'tradeUnionCount',
]
files_tab_fields = [
    'case_text'
]

@login_required()
def add_case(request):
    if request.method=='POST':
        form = CaseForm(request.POST)
        tradeUnionForm = TradeUnionInfoForm(request.POST)
        individualForm = IndividualForm(request.POST)
        personGroupForm = PersonGroupForm(request.POST)
        companyInfoForm = CompanyInfoForm(request.POST)
        casePhotoForm = CasePhotoForm(request.POST)
        caseFileForm = CaseFileForm(request.POST)

        if form.is_valid():
            form = form.save(commit=False)

            if tradeUnionForm.is_valid():
                form.tradeUnionInfo = tradeUnionForm.save()
            if personGroupForm.is_valid():
                form.groupOfPersons = personGroupForm.save()
            if companyInfoForm.is_valid():
                form.company = companyInfoForm.save()

            form.user = request.user
            form.save()

            if individualForm.is_valid():
                individualForm = individualForm.save(commit=False)
                individualForm.card = form
                individualForm.save()
            # if casePhotoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CasePhoto(photo=f, card=form)
                    photo.save()
            # if caseFileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CaseFile(file=f, card=form)
                    file.save()

            return redirect('work_case')
    else:
        form = CaseForm
        tradeUnionForm = TradeUnionInfoForm
        individualForm = IndividualForm
        personGroupForm = PersonGroupForm
        companyInfoForm = CompanyInfoForm
        casePhotoForm = CasePhotoForm
        caseFileForm = CaseFileForm

    return render(request, 'work/add_case.html', context={
        'form':form,
        'tradeUnionForm':tradeUnionForm,
        'individualForm':individualForm,
        'personGroupForm':personGroupForm,
        'companyInfoForm':companyInfoForm,
        'caseFileForm':caseFileForm,
        'casePhotoForm':casePhotoForm,
        'general_tabs_fields':general_tabs_fields,
        'initiator_tab_fields':initiator_tab_fields,
        'intruder_tab_fields':intruder_tab_fields,
        'description_tab_fields':description_tab_fields,
        'files_tab_fields':files_tab_fields,
    })


@login_required()
def update_case(request,pk):

    case = Case.objects.get(id=pk)

    form = CaseForm(instance=case)


    individualForm = IndividualForm


    tradeUnionForm = TradeUnionInfoForm
    if case.tradeUnionInfo is not None:
        tradeUnionForm = TradeUnionInfoForm(instance=TradeUnionInfo.objects.get(pk=case.tradeUnionInfo_id))

    personGroupForm = PersonGroupForm
    if case.groupOfPersons is not None:
        personGroupForm = PersonGroupForm(instance=GroupOfPersons.objects.get(pk=case.groupOfPersons_id))


    companyInfoForm = CompanyInfoForm

    if case.company is not None:
        companyInfoForm = CompanyInfoForm(instance=Company.objects.get(pk=case.company_id))

    casePhotoForm = CasePhotoForm()
    caseFileForm = CaseFileForm()

    return render(request, 'work/add_case.html', context={
                            'form':form,
                            'tradeUnionForm':tradeUnionForm,
                            'individualForm':individualForm,
                            'personGroupForm':personGroupForm,
                            'companyInfoForm':companyInfoForm,
                            'caseFileForm':caseFileForm,
                            'casePhotoForm':casePhotoForm,
                            'general_tabs_fields':general_tabs_fields,
                            'initiator_tab_fields':initiator_tab_fields,
                            'intruder_tab_fields':intruder_tab_fields,
                            'description_tab_fields':description_tab_fields,
                            'files_tab_fields':files_tab_fields,
                        })


def delete_case(request,pk ):
    pass

def cases(request):
    cases = Case.objects.all().filter(user=request.user)

    filter = WorkFilter(request.GET, queryset=cases)
    cards = filter.qs

    context = {'cards': cards, 'myFilter': filter}

    return render(request, 'work/cases.html', context)



def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id).all()
    return render(request,'work/region_dropdown.html',{'regions':regions})