from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.

from .forms import CaseForm, IndividualForm, PersonGroupForm, TradeUnionInfoForm
from .models import *


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
        'case_date',
    ]
    initiator_tab_fields = [
        'victim'
    ]


    if request.method=='POST':
        pass
    else:
        form = CaseForm
        tradeUnionForm = TradeUnionInfoForm
        individualForm = IndividualForm
        personGroupForm = PersonGroupForm

    return render(request, 'work/add_case.html', context={
        'form':form,
        'tradeUnionForm':tradeUnionForm,
        'individualForm':individualForm,
        'personGroupForm':personGroupForm,
        'general_tabs_fields':general_tabs_fields,
        'initiator_tab_fields':initiator_tab_fields,
    })

def cases(request):
    pass