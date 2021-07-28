from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
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

            form.save_m2m()




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

            form.save_m2m()




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
    card_comment = CardComment.objects.get(id=pk).delete()
    card_comment.save()
    return redirect('strike_card_show_comments', card_comment.card_id)


def case_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    comments = CardComment.objects.filter(card_id=pk)
    template_path = 'strike/strike_pdf.html'
    context = {'card': card, 'comments': comments}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        BytesIO(html.encode('UTF-8')), dest=response, encoding='utf-8')
        # StringIO(html.encode("UTF-8")), response, encoding='UTF-8')
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def case_download_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    template_path = 'strike/strike_pdf.html'
    context = {'card': card}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        BytesIO(html.encode('UTF-8')), dest=response, encoding='utf-8')
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


class DataAPIView(APIView):
    def get(self, request):
        country = CountrySerializers(Country.objects.all(), many=True)
        region = RegionSerializers(Region.objects.all(), many=True)
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
            {'id': 'region', 'name': 'Регион', 'item': {1: [
                {
                    "id": 1,
                    "name": "г.Москва"
                },
                {
                    "id": 2,
                    "name": "Амурскаяобласть(Благовещенск)"
                },
                {
                    "id": 3,
                    "name": "Архангельскаяобласть(Архангельск)"
                },
                {
                    "id": 4,
                    "name": "Астраханскаяобласть(Астрахань)"
                },
                {
                    "id": 5,
                    "name": "Белгородскаяобласть(Белгород)"
                },
                {
                    "id": 6,
                    "name": "Брянскаяобласть(Брянск)"
                },
                {
                    "id": 7,
                    "name": "Челябинскаяобласть(Челябинск)"
                },
                {
                    "id": 8,
                    "name": "Иркутскаяобласть(Иркутск)"
                },
                {
                    "id": 9,
                    "name": "Ивановскаяобласть(Иваново)"
                },
                {
                    "id": 10,
                    "name": "Калининградскаяобласть(Калининград)"
                },
                {
                    "id": 11,
                    "name": "Калужскаяобласть(Калуга)"
                },
                {
                    "id": 12,
                    "name": "Кемеровскаяобласть—Кузбасс(Кемерово)"
                },
                {
                    "id": 13,
                    "name": "Кировскаяобласть(Киров)"
                },
                {
                    "id": 14,
                    "name": "Костромскаяобласть(Кострома)"
                },
                {
                    "id": 15,
                    "name": "Курганскаяобласть(Курган)"
                },
                {
                    "id": 16,
                    "name": "Курскаяобласть(Курск)"
                },
                {
                    "id": 17,
                    "name": "Ленинградскаяобласть(Санкт Петербург)"
                },
                {
                    "id": 19,
                    "name": "Липецкаяобласть(Липецк)"
                },
                {
                    "id": 20,
                    "name": "Магаданскаяобласть(Магадан)"
                },
                {
                    "id": 21,
                    "name": "Московскаяобласть(Москва)"
                },
                {
                    "id": 22,
                    "name": "Мурманскаяобласть(Мурманск)"
                },
                {
                    "id": 23,
                    "name": "Нижегородскаяобласть(НижнийНовгород)"
                },
                {
                    "id": 24,
                    "name": "Новгородскаяобласть(ВеликийНовгород)"
                },
                {
                    "id": 25,
                    "name": "Новосибирскаяобласть(Новосибирск)"
                },
                {
                    "id": 26,
                    "name": "Омскаяобласть(Омск)"
                },
                {
                    "id": 27,
                    "name": "Оренбургскаяобласть(Оренбург)"
                },
                {
                    "id": 28,
                    "name": "Орловскаяобласть(Орёл)"
                },
                {
                    "id": 29,
                    "name": "Пензенскаяобласть(Пенза)"
                },
                {
                    "id": 30,
                    "name": "Псковскаяобласть(Псков)"
                },
                {
                    "id": 31,
                    "name": "Ростовскаяобласть(Ростов на Дону)"
                },
                {
                    "id": 32,
                    "name": "Рязанскаяобласть(Рязань)"
                },
                {
                    "id": 33,
                    "name": "Сахалинскаяобласть(Южно Сахалинск)"
                },
                {
                    "id": 34,
                    "name": "Самарскаяобласть(Самара)"
                },
                {
                    "id": 35,
                    "name": "Саратовскаяобласть(Саратов)"
                },
                {
                    "id": 36,
                    "name": "Смоленскаяобласть(Смоленск)"
                },
                {
                    "id": 37,
                    "name": "Свердловскаяобласть(Екатеринбург)"
                },
                {
                    "id": 38,
                    "name": "Тамбовскаяобласть(Тамбов)"
                },
                {
                    "id": 39,
                    "name": "Томскаяобласть(Томск)"
                },
                {
                    "id": 40,
                    "name": "Тверскаяобласть(Тверь)"
                },
                {
                    "id": 41,
                    "name": "Тульскаяобласть(Тула)"
                },
                {
                    "id": 42,
                    "name": "Тюменскаяобласть(Тюмень)"
                },
                {
                    "id": 43,
                    "name": "Ульяновскаяобласть(Ульяновск)"
                },
                {
                    "id": 44,
                    "name": "Владимирскаяобласть(Владимир)"
                },
                {
                    "id": 45,
                    "name": "Волгоградскаяобласть(Волгоград)"
                },
                {
                    "id": 46,
                    "name": "Вологодскаяобласть(Вологда)"
                },
                {
                    "id": 47,
                    "name": "Воронежскаяобласть(Воронеж)"
                },
                {
                    "id": 48,
                    "name": "Ярославскаяобласть(Ярославль)"
                }
            ],
                2: [
                    {
                        "id": 49,
                        "name": "г. Бишкек"
                    },
                    {
                        "id": 50,
                        "name": "г. Ош"
                    },
                    {
                        "id": 51,
                        "name": "Баткенская область"
                    },
                    {
                        "id": 52,
                        "name": "Джалал-Абадская область"
                    },
                    {
                        "id": 53,
                        "name": "Иссык-Кульская область"
                    },
                    {
                        "id": 54,
                        "name": "Нарынская область"
                    },
                    {
                        "id": 55,
                        "name": "Ошская область"
                    },
                    {
                        "id": 56,
                        "name": "Таласская область"
                    },
                    {
                        "id": 57,
                        "name": "Чуйская область"
                    }],
                3: [
                    {
                        "id": 58,
                        "name": "Нур-Султан (Астана)"
                    },
                    {
                        "id": 59,
                        "name": "Алматы"
                    },
                    {
                        "id": 60,
                        "name": "Шымкент"
                    },
                    {
                        "id": 61,
                        "name": "Байконыр"
                    },
                    {
                        "id": 62,
                        "name": "Акмолинская область"
                    },
                    {
                        "id": 63,
                        "name": "Актюбинская область"
                    },
                    {
                        "id": 64,
                        "name": "Алматинская область"
                    },
                    {
                        "id": 65,
                        "name": "Атырауская область"
                    },
                    {
                        "id": 66,
                        "name": "Восточно-Казахстанская область"
                    },
                    {
                        "id": 67,
                        "name": "Жамбылская область"
                    },
                    {
                        "id": 68,
                        "name": "Западно-Казахстанская область"
                    },
                    {
                        "id": 69,
                        "name": "Карагандинская область"
                    },
                    {
                        "id": 70,
                        "name": "Костанайская область"
                    },
                    {
                        "id": 71,
                        "name": "Кызылординская область"
                    },
                    {
                        "id": 72,
                        "name": "Мангистауская область"
                    },
                    {
                        "id": 73,
                        "name": "Павлодарская область"
                    },
                    {
                        "id": 74,
                        "name": "Севрено-Казахстанская область"
                    },
                    {
                        "id": 75,
                        "name": "Туркестанская область"
                    }],
                4: [
                    {
                        "id": 76,
                        "name": "г. Душанбе"
                    },
                    {
                        "id": 77,
                        "name": "Горно - Бажахшанская область"
                    },
                    {
                        "id": 78,
                        "name": "Согдийская область"
                    },
                    {
                        "id": 79,
                        "name": "Хатлонская область"
                    },
                    {
                        "id": 80,
                        "name": "Районы республиканского подчинения"
                    }],
                5: [
                    {
                        "id": 81,
                        "name": "г. Ашхабад"
                    },
                    {
                        "id": 82,
                        "name": "Ахалский велаят"
                    },
                    {
                        "id": 83,
                        "name": "Балканский велаят"
                    },
                    {
                        "id": 84,
                        "name": "Дашогузский велаят"
                    },
                    {
                        "id": 85,
                        "name": "Лебапский велаят"
                    },
                    {
                        "id": 86,
                        "name": "Марыйский велаят"
                    }
                ]
            }},
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
        case_count = Card.objects.count()
        sql_query = f"SELECT {fields}, count(*), round(count (*) * 100.0 /{case_count}, 2) percent FROM strike_card"
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
        print(sql_query + where_query + group_by_query)
        with connection.cursor() as cursor:
            cursor.execute(
                sql_query + where_query + group_by_query
            )
            row = cursor.fetchall()
            print(row)
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

        # return Response(status=401)
        return Response(response_list)


def card_files_download(request, pk):
    case = Card.objects.get(added_by=request.user, pk=pk)
    images = CardPhoto.objects.filter(card_id=case.id)
    files = CardFile.objects.filter(card_id=case.id)
    return render(request, 'migrant/files_download.html', {'images': images, 'files': files})
