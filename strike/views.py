from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.forms import model_to_dict
from django.shortcuts import render
from django_filters.views import FilterView
from django_tables2 import SingleTableView
from django_tables2.views import SingleTableMixin

import json

from .filters import CardFilter
from .forms import *
from .models import *
from .tables import CardTable


def append_region(request):
    # countries = Country.objects.all()
    # country_json = serialize('json', countries)
    countries = Country.objects.all()
    country_json = serialize('json', Country.objects.all())

    cleaned_data = []
    if request.method == 'POST':
        form = RegionForm(request.POST)

        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            cleaned_data['country'] = form.cleaned_data['country'].id
            print('save')


    else:
        form = RegionForm()


    return render(request, "strike/test.html",
                  {
                      'form':form,
                      'country_json':country_json,
                      'cleaned_data':cleaned_data
                  })


def get_cleaned_data(queryset, mode):
    if mode == 1:
        result_list = []
        for item in queryset:
            result_list.append(model_to_dict(item))
        return result_list
    pass


@login_required
def append_case(request):
    country_json = serialize('json', Country.objects.all().filter(active=True))
    region_json = serialize('json', Region.objects.all().filter(active=True))
    ownership_json = serialize('json', OwnerShipType.objects.all().filter(active=True))
    employeeCount_json = serialize('json', EmployeesCount.objects.all().filter(active=True))
    participantsCount_json = serialize('json', ParticipantsCount.objects.all().filter(active=True))
    demandType_json = serialize('json', DemandType.objects.all().filter(active=True))
    demandCategory_json = serialize('json', DemandCategory.objects.all().filter(active=True))
    hasTradeUnionChoice_json = serialize('json', TradeunionChoice.objects.all().filter(active=True))
    personGroup_json = serialize('json', PersonGroup.objects.all().filter(active=True))
    groupCharacter_json = serialize('json', GroupCharacter.objects.all().filter(active=True))
    age_json = serialize('json', Age.objects.all().filter(active=True))
    strikeCharacter_json = serialize('json', StrikeCharacter.objects.all().filter(active=True))
    meetingRequirment_json = serialize('json', MeetingRequirment.objects.all().filter(active=True))
    source_json = serialize('json', Source.objects.all().filter(active=True))
    initiator_json = serialize('json', Initiator.objects.all())
    cleaned_data = []

    if request.method == 'POST':
        form = CardForm(request.POST)
        tradeunionForm=TradeunionForm(request.POST)
        if form.is_valid():
              #cleaned_data['demandType'] = get_cleaned_data(form.cleaned_data['demandType'], 1)

            # source_list1 = json.dumps(cleaned_data['card_sources'])
            # print(source_list1)
            card = form.save(commit=False)
            card.added_by = request.user
            card.save()

            #return redirect('strike_case')
        else:
            cleaned_data = dict()
            cleaned_data['country'] = model_to_dict(form.cleaned_data['country'])
            cleaned_data['region'] = model_to_dict(form.cleaned_data['region'])
            cleaned_data['company_ownership_type'] = model_to_dict(form.cleaned_data['company_ownership_type'])
            cleaned_data['company_employees_count'] = model_to_dict(form.cleaned_data['company_employees_count'])
            cleaned_data['count_strike_participants'] = model_to_dict(form.cleaned_data['count_strike_participants'])
            cleaned_data['tradeunionChoice'] = model_to_dict(form.cleaned_data['tradeunionChoice'])
            cleaned_data['card_sources'] = get_cleaned_data(form.cleaned_data['card_sources'], 1)
            cleaned_data['card_demand_categories'] = get_cleaned_data(form.cleaned_data['card_demand_categories'], 1)

    else:
        form = CardForm()
        tradeunionForm = TradeunionForm()

    return render(request, 'strike/strike_case_v1.html',
                  {
                      'form': form,
                      'tradeunionForm': tradeunionForm,


                      'country_json': country_json,
                      'region_json': region_json,
                      'ownership_json': ownership_json,
                      'employeeCount_json': employeeCount_json,
                      'participantsCount_json': participantsCount_json,
                      'demandType_json': demandType_json,
                      'demandCategory_json': demandCategory_json,
                      'hasTradeUnionChoice_json': hasTradeUnionChoice_json,
                      'personGroup_json': personGroup_json,
                      'groupCharacter_json': groupCharacter_json,
                      'age_json': age_json,
                      'strikeCharacter_json': strikeCharacter_json,
                      'meetingRequirment_json': meetingRequirment_json,
                      'source_json': source_json,
                      'initiator_json': initiator_json,

                      'cleaned_data':cleaned_data,
                  })
# Create your views here.

class StrikeListView(SingleTableView):
    model = Card
    table_class = CardTable
    template_name = 'strike/strikes.html'

def strikes_cases(request):
    cards = Card.objects.all()


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = CardTable
    model = Card
    template_name = "strike/strikes.html"

    filterset_class = CardFilter

@login_required
def strikes(request):
    cards = Card.objects.all()
    return render(request,'strike/strike.html', {'cards':Card.objects.all()})


def cases(request):

    cards = Card.objects.all()

    myFilter = CardFilter(request.GET,queryset=cards)
    cards = myFilter.qs

    context = {'cards':cards, 'myFilter':myFilter}

    return render(request, 'strike/strike.html', context)


