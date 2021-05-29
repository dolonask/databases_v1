from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.

from .forms import CaseForm, IndividualForm, PersonGroupForm, TradeUnionInfoForm, CompanyInfoForm, CasePhotoForm, CaseFileForm
from .models import *
from .filters import WorkFilter


def add_case(request):
    general_tabs_fields =[
        'name',
        'source',
        'source_url',
        'source_content',
        'region',
        'city_name',
        'company_name',
        'groupOfRights',
        'tradeUnionRight',
        'tradeUnionRightAnother',
        'tradeUnionCrime',
        'tradeUnionCrimeAnother',
        'meetingsRight',
        'meetingsRightAnother',
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
        'control_agency_name',
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
    files_tab_fields=[
        'case_text'
    ]


    if request.method=='POST':
        pass
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

def cases(request):
    cases = Case.objects.all().filter(user=request.user)

    filter = WorkFilter(request.GET, queryset=cases)
    cards = filter.qs

    context = {'cards': cards, 'myFilter': filter}

    return render(request, 'migrant/cases.html', context)
