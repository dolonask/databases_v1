from django.forms import model_to_dict
from django.shortcuts import render

# Create your views here.

from .forms import CaseForm, IndividualForm, GroupForm
from .models import *

def append_case(request):

    country_json = Country.objects.all().filter(active=True)
    region_json = Region.objects.all().filter(active=True)
    source_json = Source.objects.all().filter(active=True)
    groupOfRights_json = GroupOfRights.objects.all().filter(active=True)
    rightsViolation_json = RightsViolation.objects.all().filter(active=True)
    rightsViolationCase_json = RightsViolationCase.objects.all().filter(active=True)
    victim_json = Victim.objects.all().filter(active=True)
    education_json = Education.objects.all().filter(active=True)
    maritalStatus_json = MaritalStatus.objects.all().filter(active=True)
    gender_json = Gender.objects.all().filter(active=True)
    agreementDetail_json = AgreementDetail.objects.all().filter(active=True)
    groupType_json = GroupType.objects.all().filter(active=True)
    membershipOfGroupPersons_json = MembershipOfGroupPersons.objects.all().filter(active=True)
    cleaned_data=[]
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            cleaned_data = dict()
            cleaned_data['country'] = model_to_dict(form.cleaned_data['country'])
            cleaned_data['region'] = model_to_dict(form.cleaned_data['region'])
            cleaned_data['rightsViolationCase'] = model_to_dict(form.cleaned_data['rightsViolationCase'])
            cleaned_data['rightsViolation'] = model_to_dict(form.cleaned_data['rightsViolation'])
            cleaned_data['group'] = model_to_dict(form.cleaned_data['group'])

            # cleaned_data['demandType'] = get_cleaned_data(form.cleaned_data['demandType'], 1)

            # source_list1 = json.dumps(cleaned_data['card_sources'])
            # print(source_list1)
            card = form.save(commit=False)
            card.added_by = request.user
            card.save()

            # return redirect('strike_case')
    else:
        form = CaseForm
        individualForm = IndividualForm
        groupForm = GroupForm

    return render(request,
                  'work/append_case.html',
                  context={
                      'form': form,
                      'country_json': country_json,
                      'region_json': region_json,
                      'groupType_json': groupType_json,
                      'source_json': source_json,
                      'victim_json': victim_json,
                      'education_json': education_json,
                      'membershipOfGroupPersons_json': membershipOfGroupPersons_json,
                      'agreementDetail_json': agreementDetail_json,
                      'maritalStatus_json': maritalStatus_json,
                      'rightsViolationCase_json': rightsViolationCase_json,
                      'groupOfRights_json': groupOfRights_json,
                      'rightsViolation_json': rightsViolation_json,
                      'gender_json': gender_json,
                      'individualForm': individualForm,
                      'groupForm': groupForm,
                      'cleaned_data':cleaned_data
                  })


def cases(request):
    pass