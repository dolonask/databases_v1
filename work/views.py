from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.

from .forms import CaseForm, IndividualForm, GroupForm
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
    ]


    if request.method=='POST':
        pass
    else:
        form = CaseForm

    return render(request, 'work/add_case.html', context={
        'form':form,
        'general_tabs_fields':general_tabs_fields,
    })

def cases(request):
    pass