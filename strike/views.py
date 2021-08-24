from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from io import BytesIO, StringIO
from django.template.loader import get_template
from xhtml2pdf import pisa
from rest_framework.views import APIView
from rest_framework.response import Response
from main.service import unpucking
from .serializers import *
from .filters import CardFilter
from django.db import connection
from .forms import *
from .models import *
from docxtpl import DocxTemplate
from migrant.templatetags.migrant_tags import var_verbose_name_for_word
import jinja2
import os
import pdfkit

@login_required()
def add_case(request):
    general_tabs_fields = ['name',
                           'card_sources',
                           'source_url',
                           'source_content',
                           'country',
                           'region',
                           'city_name',
                           'company_name',
                           'company_ownership_type',
                           'company_is_tnk_member',
                           'company_tnk_name',
                           'company_employees_count',
                           'count_strike_participants',
                           'card_demand_categories',
                           'economic_demands',
                           'politic_demands',
                           'combo_demands',
                           'start_date',
                           'end_date',
                           'tradeunionChoice',
                           'tradeunionChoiceAnother',
                           'economic_another',
                           'politic_another',
                           'combo_another',
                           ]
    initiator_tab_fields = ['initiator']
    description_tab_fields = ['duration',
                              'meeting_requirements',
                              'story',
                              'reasons_for_strike',
                              'change_number_participants',
                              'initiators_and_participants',
                              'state_position',
                              'results_so_far',
                              'additional_information',

                              ]
    if request.method == "POST":
        form = CardForm(request.POST)
        tradeUnionForm = TradeunionForm(request.POST)
        personGroupInfoForm = PersonGroupInfoForm(request.POST)
        # individualForm = IndividualForm(request.POST)

        individualFormSet = IndividualFormSet(data=request.POST)


        employerForm = EmployerForm(request.POST)
        photoForm = CardPhotoForm(request.POST)
        fileForm = CardFileForm(request.POST)

        if form.is_valid():
            case = form.save(commit=False)

            if tradeUnionForm.is_valid():
                case.tradeunion_data = tradeUnionForm.save()
            if personGroupInfoForm.is_valid():
                case.personGroupInfo = personGroupInfoForm.save()
            # if individualFormSet.is_valid():
            #     for individualForm in individualFormSet.forms:
            #         ind = individualForm.save(commit = False)
            #         ind.card = case
            #         ind.save()

            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.card = case
            # individualFormSet.save()
            if employerForm.is_valid():
                case.employear = employerForm.save()


            case.added_by = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form._save_m2m()




            # if individualForm.is_valid():
            #     individualForm = individualForm.save(commit=False)
            #     individualForm.card = form
            #     individualForm.save()
            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CardPhoto(photo=f, card=case)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CardFile(file=f, card=case)
                    file.save()

            return redirect('strikes_list')
    else:
        form = CardForm
        tradeUnionForm = TradeunionForm
        personGroupInfoForm = PersonGroupInfoForm
        individualFormSet = IndividualFormSet(queryset=Individual.objects.none())
        employerForm = EmployerForm
        photoForm = CardPhotoForm
        fileForm = CardFileForm

    return render(request,'strike/add_case.html', context={
        'form':form,
        'tradeUnionForm':tradeUnionForm,
        'personGroupInfoForm':personGroupInfoForm,
        'individualFormSet':individualFormSet,
        'employerForm':employerForm,
        'photoForm':photoForm,
        'fileForm':fileForm,
        'general_tabs_fields':general_tabs_fields,
        'initiator_tab_fields':initiator_tab_fields,
        'description_tab_fields':description_tab_fields,
    })


def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id).all()
    return render(request,'strike/region_dropdown.html',{'regions':regions})


@login_required()
def cases(request):
    if request.user.position.role_id == 1:
        cards = Card.objects.all()
        myFilter = CardFilter(request.GET, queryset=cards)
        cards = myFilter.qs
        context = {'cards': cards, 'myFilter': myFilter}
        return render(request, 'strike/strike.html', context)
    elif request.user.position.role_id == 2 or request.user.position.role_id == 3:
        cards = Card.objects.filter(country_id=request.user.country.country_id)
        myFilter = CardFilter(request.GET, queryset=cards)
        cards = myFilter.qs
        context = {'cards': cards, 'myFilter': myFilter}
        return render(request, 'strike/strike.html', context)


@login_required()
def delete_case(request, pk):
    case = Card.objects.get(id=pk).delete()
    return redirect('strikes_list')

@login_required()
def update_case(request, pk):
    case = Card.objects.get(id=pk)
    general_tabs_fields = ['name',
                           'card_sources',
                           'source_url',
                           'source_content',
                           'country',
                           'region',
                           'city_name',
                           'company_name',
                           'company_ownership_type',
                           'company_is_tnk_member',
                           'company_tnk_name',
                           'company_employees_count',
                           'count_strike_participants',
                           'card_demand_categories',
                           'economic_demands',
                           'politic_demands',
                           'combo_demands',
                           'start_date',
                           'end_date',
                           'tradeunionChoice',
                           'tradeunionChoiceAnother',
                           'economic_another',
                           'politic_another',
                           'combo_another',
                           ]
    initiator_tab_fields = ['initiator']
    description_tab_fields = ['duration',
                              'meeting_requirements',
                              'story',
                              'reasons_for_strike',
                              'change_number_participants',
                              'initiators_and_participants',
                              'state_position',
                              'results_so_far',
                              'additional_information',

                              ]
    if request.method == "POST":
        form = CardForm(request.POST, instance=case)
        tradeUnionForm = TradeunionForm(request.POST)
        personGroupInfoForm = PersonGroupInfoForm(request.POST)
        # individualForm = IndividualForm(request.POST)

        individualFormSet = IndividualFormSet(data = request.POST)


        employerForm = EmployerForm(request.POST)
        photoForm = CardPhotoForm(request.POST)
        fileForm = CardFileForm(request.POST)

        if form.is_valid():
            form.save(commit=False)

            if tradeUnionForm.is_valid():
                case.tradeunion_data = tradeUnionForm.save()
            if personGroupInfoForm.is_valid():
                case.personGroupInfo = personGroupInfoForm.save()
            # if individualFormSet.is_valid():
            #     for individualForm in individualFormSet.forms:
            #         ind = individualForm.save(commit = False)
            #         ind.card = case
            #         ind.save()

            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.card = case
            # individualFormSet.save()
            if employerForm.is_valid():
                case.employear = employerForm.save()


            case.added_by = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form._save_m2m()




            # if individualForm.is_valid():
            #     individualForm = individualForm.save(commit=False)
            #     individualForm.card = form
            #     individualForm.save()
            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CardPhoto(photo=f, card=form)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CardFile(file=f, card=form)
                    file.save()

            return redirect('strikes_list')
    else:
        form = CardForm(instance=case)

        tradeUnionForm = TradeunionForm
        if case.tradeunion_data is not None:
            tradeUnionForm = TradeunionForm(instance=TradeunionData.objects.get(pk = case.tradeunion_data_id))

        personGroupInfoForm = PersonGroupInfoForm
        if case.personGroupInfo is not None:
            personGroupInfoForm = PersonGroupInfoForm(instance=PersonGroupInfo.objects.get(pk=case.personGroupInfo_id))

        individualForm = IndividualForm
        # if Individual.objects.exists(card=case.pk):
        #     individualForm = IndividualForm(instance=Individual.objects.get(card=case.pk))

        employerForm = EmployerForm
        if case.employear is not None:
            employerForm = EmployerForm(instance=Employer.objects.get(pk=case.employear_id))

        photoForm = CardPhotoForm
        fileForm = CardFileForm

    return render(request, 'strike/add_case.html', context={
        'form': form,
        'tradeUnionForm': tradeUnionForm,
        'personGroupInfoForm': personGroupInfoForm,
        'individualForm': individualForm,
        'employerForm': employerForm,
        'photoForm': photoForm,
        'fileForm': fileForm,
        'general_tabs_fields': general_tabs_fields,
        'initiator_tab_fields': initiator_tab_fields,
        'description_tab_fields': description_tab_fields,
    })

@login_required()
def add_comment(request, pk):
    card = Card.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data['card'] = card.id
        form = CardCommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('strikes_list')
    else:
        form = CardCommentForm()
    return render(request, 'strike/add_comment.html', {'form': form, 'card': card})


def show_comments(request, pk):
    comments = CardComment.objects.filter(card_id=pk, active=True)
    return render(request, 'strike/show_comments.html', {'comments': comments})


def delete_comment(request, pk):
    CardComment.objects.get(id=pk).delete()
    return redirect('strikes_list')


def case_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    card_sources = Source.objects.filter(card__pk=pk)
    card_demand_categories = DemandCategory.objects.filter(card__pk=pk)
    economic_demands = EconomicDemand.objects.filter(card__pk=pk)
    politic_demands = PoliticDemand.objects.filter(card__pk=pk)
    combo_demands = ComboDemand.objects.filter(card__pk=pk)
    comments = CardComment.objects.filter(card_id=pk)
    template_path = 'strike/strike_pdf.html'
    context = {
        'card': card,
        'card_sources': card_sources,
        'card_demand_categories': card_demand_categories,
        'economic_demands': economic_demands,
        'politic_demands': politic_demands,
        'combo_demands': combo_demands,
        'comments': comments,
    }
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="card_{card.id}.pdf"'
    # StringIO(html.encode("UTF-8")), response, encoding='UTF-8')
    # if error then show some funy view
    return response


def case_download_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    card_sources = Source.objects.filter(card__pk=pk)
    card_demand_categories = DemandCategory.objects.filter(card__pk=pk)
    economic_demands = EconomicDemand.objects.filter(card__pk=pk)
    politic_demands = PoliticDemand.objects.filter(card__pk=pk)
    combo_demands = ComboDemand.objects.filter(card__pk=pk)
    comments = CardComment.objects.filter(card_id=pk)
    template_path = 'strike/strike_pdf.html'
    context = {
        'card': card,
        'card_sources': card_sources,
        'card_demand_categories': card_demand_categories,
        'economic_demands': economic_demands,
        'politic_demands': politic_demands,
        'combo_demands': combo_demands,
        'comments': comments,
    }
    # Create a Django response object, and specify content_type as pdf
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="card_{card.id}.pdf"'
    return response

class DataAPIView(APIView):
    def get(self, request):
        country = CountrySerializers(Country.objects.all(), many=True)
        region_1 = RegionSerializers(Region.objects.filter(country__pk=1), many=True)
        region_2 = RegionSerializers(Region.objects.filter(country__pk=2), many=True)
        region_3 = RegionSerializers(Region.objects.filter(country__pk=3), many=True)
        region_4 = RegionSerializers(Region.objects.filter(country__pk=4), many=True)
        region_5 = RegionSerializers(Region.objects.filter(country__pk=5), many=True)
        source = SourceSerializers(Source.objects.all(), many=True)
        added_by = UserSerializers(User.objects.all(), many=True)
        demand_categories = DemandCategorySerializers(DemandCategory.objects.all(), many=True)
        economic_demands = EconomicDemandSerializers(EconomicDemand.objects.all(), many=True)
        politic_demands = PoliticDemandSerializers(PoliticDemand.objects.all(), many=True)
        combo_demands = ComboDemandSerializers(ComboDemand.objects.all(), many=True)
        company_ownership_type = OwnerShipTypeSerializers(OwnerShipType.objects.all(), many=True)
        company_employees_count = EmployeesCountSerializers(EmployeesCount.objects.all(), many=True)
        count_strike_participants = ParticipantsCountSerializers(ParticipantsCount.objects.all(), many=True)
        tradeunion_choice = TradeunionChoiceSerializers(TradeunionChoice.objects.all(), many=True)
        initiator = InitiatorSerializers(Initiator.objects.all(), many=True)
        tradeunion_data = TradeunionDataSerializers(TradeunionData.objects.all(), many=True)
        employear = EmployerSerializers(Employer.objects.all(), many=True)
        duration = StrikeCharacterSerializers(StrikeCharacter.objects.all(), many=True)
        meeting_requirements = MeetingRequirmentSerializers(MeetingRequirment.objects.all(), many=True)
        # personGroupInfo = Группа лиц
        return Response([
            {'id': 'country', 'name': 'Страна', 'item': country.data},
            {'id': 'region', 'name': 'Регион', 'item': {1: region_1.data,
                                                        2: region_2.data,
                                                        3: region_3.data,
                                                        4: region_4.data,
                                                        5: region_5.data}},
            {'id': 'source', 'name': 'Источник', 'item': source.data},
            {'id': 'user', 'name': 'Монитор', 'item': added_by.data},
            {'id': 'demand_cat', 'name': 'Характер требований', 'item': demand_categories.data},
            {'id': 'economicdemand', 'name': 'Экономический', 'item': economic_demands.data},
            {'id': 'politicdemand', 'name': 'Политический', 'item': politic_demands.data},
            {'id': 'combodemand', 'name': 'Смешанный', 'item': combo_demands.data},
            {'id': 'ownershiptype', 'name': 'Форма собственности компании', 'item': company_ownership_type.data},
            {'id': 'employeescount', 'name': 'Общая численность работников на предприятии', 'item': company_employees_count.data},
            {'id': 'participantscount', 'name': 'Общая численность работников на предприятии', 'item': count_strike_participants.data},
            {'id': 'tradeunionchoice', 'name': 'Есть ли на предприятии профсоюз', 'item': tradeunion_choice.data},
            {'id': 'initiator', 'name': 'Инициатор забастовки/акции', 'item': initiator.data},
            {'id': 'tradeuniondata', 'name': 'Данные профсоюза', 'item': tradeunion_data.data},
            {'id': 'employer', 'name': 'Работодатель', 'item': employear.data},
            {'id': 'strikecharacter', 'name': 'Характер забастовки/акции - сколько длилась', 'item': duration.data},
            {'id': 'meetingrequirment', 'name': 'Удовлетворение требований', 'item': meeting_requirements.data},
        ])


class DataFilterAPI(APIView):
    authentication_classes = []
    def post(self, request):
        my_list = []
        print(request.data)
        for item in request.data:
            if item['id'] == 'user':
                my_list.append(f"auth_user.username")
            elif item['id'] == 'demand_cat':
                my_list.append(f"strike_demandcategory.demand_cat_name")
            elif item['id'] == 'economicdemand':
                my_list.append(f"strike_economicdemand.name")
            elif item['id'] == 'politicdemand':
                my_list.append(f"strike_politicdemand.name")
            elif item['id'] == 'combodemand':
                my_list.append(f"strike_combodemand.name")
            elif item['id'] == 'ownershiptype':
                my_list.append(f"strike_ownershiptype.name")
            elif item['id'] == 'employeescount':
                my_list.append(f"strike_employeescount.choice")
            elif item['id'] == 'participantscount':
                my_list.append(f"strike_participantscount.choice")
            elif item['id'] == 'tradeuniondata':
                my_list.append(f"strike_tradeuniondata.tradeUnion_name")
            elif item['id'] == 'employer':
                my_list.append(f"strike_employer.emp_name")

            else:
                my_list.append(f"strike_{item['id']}.name")
        fields = unpucking(my_list)
        # case_count = Card.objects.count()
        sql_query = f"SELECT {fields}, count(*), 100 / count (*) FROM strike_card"
        where_query = "where "
        where_list = []
        where_query_list = []
        group_by_query = f"group by {fields}"
        for data in request.data:
            if data['id'] in fields:
                id = data['id']
                item = data['item']
                if id == "country":
                    where_sql_query = "strike_card.country_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_country on strike_country.id = strike_card.country_id "

                elif id == "region":
                    where_sql_query = "strike_card.region_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_region on strike_region.id = strike_card.region_id "

                elif id == "user":
                    where_sql_query = "strike_card.added_by_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join auth_user on auth_user.id = strike_card.added_by_id "

                elif id == "ownershiptype":
                    where_sql_query = "strike_card.company_ownership_type_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_ownershiptype on strike_ownershiptype.id = strike_card.company_ownership_type_id "

                elif id == "employeescount":
                    where_sql_query = "strike_card.company_employees_count_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_employeescount on strike_employeescount.id = strike_card.company_employees_count_id "

                elif id == "participantscount":
                    where_sql_query = "strike_card.count_strike_participants_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_participantscount on strike_participantscount.id = strike_card.count_strike_participants_id "

                elif id == "tradeunionchoice":
                    where_sql_query = "strike_card.tradeunionChoice_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_tradeunionchoice on strike_tradeunionchoice.id = strike_card.tradeunionChoice_id "

                elif id == "initiator":
                    where_sql_query = "strike_card.initiator_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_initiator on strike_initiator.id = strike_card.initiator_id "

                elif id == "tradeuniondata":
                    where_sql_query = "strike_card.tradeunion_data_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_tradeuniondata on strike_tradeuniondata.id = strike_card.tradeunion_data_id "

                elif id == "employer":
                    where_sql_query = "strike_card.employear_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_employer on strike_employer.id = strike_card.employear_id "

                elif id == "strikecharacter":
                    where_sql_query = "strike_card.duration_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_strikecharacter on strike_strikecharacter.id = strike_card.duration_id "

                elif id == "meetingrequirment":
                    where_sql_query = "strike_card.meeting_requirements_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_meetingrequirment on strike_meetingrequirment.id = strike_card.meeting_requirements_id "


                # elif id == "": # Экземпляр
                #     where_sql_query = "strike_card._id in "
                #     for i in item:
                #         where_list.append(i['id'])
                #     if len(where_list) > 1:
                #         where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                #     else:
                #         where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                #     where_list.clear()
                #     sql_query += " join strike_ on strike_.id = strike_card._id "


                # Ниже представлены ManyToMany связи!
                elif id == "source":
                    where_sql_query = "strike_card_card_sources.source_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_card_card_sources on strike_card.id = strike_card_card_sources.card_id join strike_source on strike_card_card_sources.source_id = strike_source.id "

                elif id == "demand_cat":
                    where_sql_query = "strike_card_card_demand_categories.demandcategory_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_card_card_demand_categories on strike_card.id = strike_card_card_demand_categories.card_id join strike_demandcategory on strike_card_card_demand_categories.demandcategory_id = strike_demandcategory.id "

                elif id == "economicdemand":
                    where_sql_query = "strike_card_economic_demands.economicdemand_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_card_economic_demands on strike_card.id = strike_card_economic_demands.card_id join strike_economicdemand on strike_card_economic_demands.economicdemand_id = strike_economicdemand.id "

                elif id == "politicdemand":
                    where_sql_query = "strike_card_politic_demands.politicdemand_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_card_politic_demands on strike_card.id = strike_card_politic_demands.card_id join strike_politicdemand on strike_card_politic_demands.politicdemand_id = strike_politicdemand.id "

                elif id == "combodemand":
                    where_sql_query = "strike_card_combo_demands.combodemand_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join strike_card_combo_demands on strike_card.id = strike_card_combo_demands.card_id join strike_combodemand on strike_card_combo_demands.combodemand_id = strike_combodemand.id "

            else:
                continue
        where_query_list = 'and '.join(where_query_list)
        where_query += where_query_list
        # print(where_query)
        # print(sql_query + where_query + group_by_query)
        with connection.cursor() as cursor:
            cursor.execute(
                sql_query + where_query + group_by_query
            )
            row = cursor.fetchall()
            # print(row)
            fields_list = []
            for i in request.data:
                fields_list.append(i['id'])
            fields_list.append('count')
            fields_list.append('percent')
            response_list = []

            for i in range(len(row)):
                response_body = dict()
                for j in range(len(fields_list)):
                    response_body[fields_list[j]] = row[i][j]
                response_list.append(response_body)
            for i in range(len(response_list)):
                response_list[i]['percent'] = 100 / len(response_list)
        # return Response(status=401)
        return Response(response_list)


def card_files_download(request, pk):
    if request.user.position.role_id == 3:
        case = Card.objects.get(added_by=request.user, id=pk)
        images = CardPhoto.objects.filter(card_id=case.id)
        files = CardFile.objects.filter(card_id=case.id)
        return render(request, 'migrant/files_download.html', {'images': images, 'files': files})
    else:
        case = Card.objects.get(id=pk)
        images = CardPhoto.objects.filter(card_id=case.id)
        files = CardFile.objects.filter(card_id=case.id)
        return render(request, 'migrant/files_download.html', {'images': images, 'files': files})


def generate_card_word(request, pk):
    card = Card.objects.get(id=pk)
    card_sources = Source.objects.filter(card__pk=pk)
    card_demand_categories = DemandCategory.objects.filter(card__pk=pk)
    economic_demands = EconomicDemand.objects.filter(card__pk=pk)
    politic_demands = PoliticDemand.objects.filter(card__pk=pk)
    combo_demands = ComboDemand.objects.filter(card__pk=pk)
    comments = CardComment.objects.filter(card_id=pk)
    base_dir = str(settings.BASE_DIR)
    base_dir += "/strike/static/word/strike/"
    tpl = DocxTemplate(base_dir + 'template.docx')
    context = {
        'card': card,
        'card_sources': card_sources,
        'card_demand_categories': card_demand_categories,
        'economic_demands': economic_demands,
        'politic_demands': politic_demands,
        'combo_demands': combo_demands,
        'comments': comments,
    }
    jinja_env = jinja2.Environment()
    jinja_env.filters['var_verbose_name'] = var_verbose_name_for_word
    tpl.render(context, jinja_env=jinja_env)
    save_path = base_dir + f'card_{card.id}.docx'
    tpl.save(save_path)
    if os.path.exists(save_path):
        with open(save_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(save_path)
            return response
    return Http404()
