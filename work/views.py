from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from django.template.loader import get_template
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from django.core import serializers
from xhtml2pdf import pisa
from io import BytesIO
from django.contrib.auth.models import User
import json
from django.db import connection
from main.service import unpucking


from .filters import WorkFilter
from .forms import CaseForm, IndividualForm, PersonGroupForm, TradeUnionInfoForm, CompanyInfoForm, CasePhotoForm, \
    CaseFileForm, IndividualFormSet, CaseCommentForm
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
    'tradeunion_actions',
    'case_result',
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
        individualFormSet = IndividualFormSet(data=request.POST)
        personGroupForm = PersonGroupForm(request.POST)
        companyInfoForm = CompanyInfoForm(request.POST)
        casePhotoForm = CasePhotoForm(request.POST)
        caseFileForm = CaseFileForm(request.POST)

        if form.is_valid():
            case = form.save(commit=False)


            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.case = case

            if tradeUnionForm.is_valid():
                case.tradeUnionInfo = tradeUnionForm.save()
            if personGroupForm.is_valid():
                case.groupOfPersons = personGroupForm.save()
            if companyInfoForm.is_valid():
                case.company = companyInfoForm.save()


            case.user = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form.save_m2m()


            # if casePhotoForm.is_valid():
            for f in request.FILES.getlist('photo'):
                photo = CasePhoto(photo=f, card=case)
                photo.save()
             # if caseFileForm.is_valid():
            for f in request.FILES.getlist('file'):
                file = CaseFile(file=f, card=case)
                file.save()

            return redirect('work_case')
    else:
        form = CaseForm
        tradeUnionForm = TradeUnionInfoForm
        individualForm = IndividualForm
        individualFormSet = IndividualFormSet(queryset=IndividualInfo.objects.none())
        personGroupForm = PersonGroupForm
        companyInfoForm = CompanyInfoForm
        casePhotoForm = CasePhotoForm
        caseFileForm = CaseFileForm
    return render(request, 'work/add_case.html', context={
        'form':form,
        'tradeUnionForm':tradeUnionForm,
        'individualFormSet':individualFormSet,
        'personGroupForm':personGroupForm,
        'companyInfoForm':companyInfoForm,
        'caseFileForm':caseFileForm,
        'casePhotoForm':casePhotoForm,
        'general_tabs_fields':general_tabs_fields,
        'initiator_tab_fields':initiator_tab_fields,
        'intruder_tab_fields':intruder_tab_fields,
        'description_tab_fields':description_tab_fields,
        'files_tab_fields':files_tab_fields,
        'individualForm': individualForm,
    })


@login_required()
def update_case(request,pk):
    case = Case.objects.get(id=pk)
    if request.method=='POST':
        form = CaseForm(request.POST, instance=case)
        tradeUnionForm = TradeUnionInfoForm(request.POST)
        individualForm = IndividualForm(request.POST)
        individualFormSet = IndividualFormSet(data=request.POST)
        personGroupForm = PersonGroupForm(request.POST)
        companyInfoForm = CompanyInfoForm(request.POST)
        casePhotoForm = CasePhotoForm(request.POST)
        caseFileForm = CaseFileForm(request.POST)

        if form.is_valid():
            form.save(commit=False)


            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.case = case

            if tradeUnionForm.is_valid():
                case.tradeUnionInfo = tradeUnionForm.save()
            if personGroupForm.is_valid():
                case.groupOfPersons = personGroupForm.save()
            if companyInfoForm.is_valid():
                case.company = companyInfoForm.save()


            case.user = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form.save_m2m()


            # if casePhotoForm.is_valid():
            for f in request.FILES.getlist('photo'):
                photo = CasePhoto(photo=f, card=case)
                photo.save()
             # if caseFileForm.is_valid():
            for f in request.FILES.getlist('file'):
                file = CaseFile(file=f, card=case)
                file.save()

            return redirect('works_list')
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


def delete_case(request, pk):
    case = Case.objects.get(id=pk).delete()
    return redirect('works_list')

def cases(request):
    if request.user.position.role_id == 1:
        cases = Case.objects.all()
        filter = WorkFilter(request.GET, queryset=cases)
        cards = filter.qs
        context = {'cards': cards, 'myFilter': filter}
        return render(request, 'work/cases.html', context)
    elif request.user.position.role_id == 2 or request.user.position.role_id == 3:
        cases = Case.objects.filter(country_id=request.user.country.country_id)
        filter = WorkFilter(request.GET, queryset=cases)
        cards = filter.qs
        context = {'cards': cards, 'myFilter': filter}
        return render(request, 'work/cases.html', context)
    else:
        raise Http404('Недостаточно прав!')


def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id).all()
    return render(request,'work/region_dropdown.html',{'regions':regions})


def add_comment(request, pk):
    case = Case.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data['case'] = case.id
        form = CaseCommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('works_list')
    else:
        form = CaseCommentForm()
    return render(request, 'work/add_comment.html', {'form': form, 'case': case})


def show_comments(request, pk):
    comments = CaseComment.objects.filter(case_id=pk, active=True)
    return render(request, 'work/show_comments.html', {'comments': comments})


def delete_comment(request, pk):
    case_comment = CaseComment.objects.get(id=pk).delete()
    return redirect('work_case_show_comments', case_comment.case_id)


def case_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    case = get_object_or_404(Case, pk=pk)
    comments = CaseComment.objects.filter(case_id=pk)
    template_path = 'work/work_pdf.html'
    context = {'case': case, 'comments': comments}
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
    case = get_object_or_404(Case, pk=pk)
    template_path = 'work/work_pdf.html'
    context = {'case': case}
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
        source = SourceSerializers(Source.objects.all(), many=True)
        country = CountrySerializers(Country.objects.all(), many=True)
        region = RegionSerializers(Region.objects.all(), many=True)
        groupOfRights = GroupOfRightsSerializers(GroupOfRights.objects.all(), many=True)
        tradeUnionRight = TradeUnionRightSerializers(TradeUnionRight.objects.all(), many=True)
        tradeUnionCrime = TradeUnionCrimeSerializers(TradeUnionCrime.objects.all(), many=True)
        meetingsRight = MeetingsRightSerializers(MeetingsRight.objects.all(), many=True)
        сonvention87 = Сonvention87Serializers(Сonvention87.objects.all(), many=True)
        tradeUnionBuildingsRight = TradeUnionBuildingsRightSerializers(TradeUnionBuildingsRight.objects.all(), many=True)
        createOrganizationRight = CreateOrganizationRightSerializers(CreateOrganizationRight.objects.all(), many=True)
        createTradeUnionRight  = CreateTradeUnionRightSerializers(CreateTradeUnionRight.objects.all(), many=True)
        electionsRight = ElectionsRightSerializers(ElectionsRight.objects.all(), many=True)
        tradeUnionActivityRight = TradeUnionActivityRightSerializers(TradeUnionActivityRight.objects.all(), many=True)
        createStrikeRight = CreateStrikeRightSerializers(CreateStrikeRight.objects.all(), many=True)
        сonvention98 = Сonvention98Serializers(Сonvention98.objects.all(), many=True)
        antiTradeUnionDiscrimination = AntiTradeUnionDiscriminationSerializers(AntiTradeUnionDiscrimination.objects.all(), many=True)
        conversationRight = СonversationRightSerializers(СonversationRight.objects.all(), many=True)
        сonvention135 = Сonvention135Serializers(Сonvention135.objects.all(), many=True)
        consultationRight = ConsultationRightSerializers(ConsultationRight.objects.all(), many=True)
        principleOfNonDiscrimination = PrincipleOfNonDiscriminationSerializers(PrincipleOfNonDiscrimination.objects.all(), many=True)
        discriminatiOnVariousGrounds = DiscriminatiOnVariousGroundsSerializers(DiscriminatiOnVariousGrounds.objects.all(), many=True)
        discriminationInVariousAreas = DiscriminationInVariousAreasSerializers(DiscriminationInVariousAreas.objects.all(), many=True)
        publicPolicyDiscrimination  = PublicPolicyDiscriminationSerializers(PublicPolicyDiscrimination.objects.all(), many=True)
        childLabor = ChildLaborSerializers(ChildLabor.objects.all(), many=True)
        сonvention138 = Сonvention138Serializers(Сonvention138.objects.all(), many=True)
        convention182 = Сonvention182Serializers(Сonvention182.objects.all(), many=True)
        prohibitionOfForcedLabor = ProhibitionOfForcedLaborSerializers(ProhibitionOfForcedLabor.objects.all(), many=True)
        useOfForcedLabor = UseOfForcedLaborSerializers(UseOfForcedLabor.objects.all(), many=True)
        governmentCoercion = GovernmentCoercionSerializers(GovernmentCoercion.objects.all(), many=True)
        violationsUsingCompulsoryLabor = ViolationsUsingCompulsoryLaborSerializer(ViolationsUsingCompulsoryLabor.objects.all(), many=True)
        failureSystemicMeasures = FailureSystemicMeasuresSerializers(FailureSystemicMeasures.objects.all(), many=True)
        victim = VictimSerializers(Victim.objects.all(), many=True)
        intruder = IntruderSerializers(Intruder.objects.all(), many=True)
        violation_nature = NatureViolationSerializers(NatureViolation.objects.all(), many=True)
        rights_state = RightsStateSerializers(RightsState.objects.all(), many=True)
        victim_situation = VictimSituationSerializers(VictimSituation.objects.all(), many=True)
        tradeUnionSituation = TradeUnionSituationSerializers(TradeUnionSituation.objects.all(), many=True)
        user = UserSerializers(User.objects.all(), many=True)
        # tradeUnionCount = TradeUnionCountSerializers(TradeUnionCount.objects.all(), many=True)
        # company = CompanySerializers(Company.objects.all(), many=True)
        # tradeUnionInfo = TradeUnionInfoSerializers(TradeUnionInfo.objects.all(), many=True)
        # groupOfPersons = GroupOfPersonsSerializers(GroupOfPersons.objects.all(), many=True)
        return Response([
            {'id': 'source', 'name': 'Источник информации', 'item': source.data},
            {'id': 'country', 'name': 'Страна', 'item': country.data},
            {'id': 'region', 'name': 'Регион', 'item': region.data},
            {'id': 'groupofrights', 'name': 'Группа прав', 'item': groupOfRights.data},
            {'id': 'tradeunionright', 'name': 'Нарушение в сфере профсоюзных прав и гражданских свобод',
             'item': tradeUnionRight.data},
            {'id': 'tradeunioncrime', 'name': 'Обвинения в преступном поведении в связи с профсоюзной деятельностью',
             'item': tradeUnionCrime.data},
            {'id': 'meetingsright', 'name': 'Нарушения права на проведение собраний и демонстраций',
             'item': meetingsRight.data},
            {'id': 'сonvention87', 'name': 'Нарушения положений Конвенции МОТ №87', 'item': сonvention87.data},
            {'id': 'tradeunionbuildingsright', 'name': 'Защита профсоюзных помещений и имущества профсоюзов',
             'item': tradeUnionBuildingsRight.data},
            {'id': 'createorganizationright', 'name': 'Создание организации без предварительного разрешения',
             'item': createOrganizationRight.data},
            {'id': 'createTradeUnionRight', 'name': 'Создание профсоюзов и вступление в профсоюзы',
             'item': createTradeUnionRight.data},
            {'id': 'electionsRight', 'name': 'Нарушение права свободно выбирать своих представителей',
             'item': electionsRight.data},
            {'id': 'tradeUnionActivityRight',
             'name': 'Нарушения права профсоюза организовывать деятельность своего аппарата',
             'item': tradeUnionActivityRight.data},
            {'id': 'createStrikeRight', 'name': 'Нарушение права на забастовку', 'item': createStrikeRight.data},
            {'id': 'сonvention98', 'name': 'Нарушения положений Конвенции МОТ №98', 'item': сonvention98.data},
            {'id': 'antiTradeUnionDiscrimination', 'name': 'Антипрофсоюзная дискриминация',
             'item': antiTradeUnionDiscrimination.data},
            {'id': 'conversationRight', 'name': 'Нарушения права на проведение коллективных переговоров',
             'item': conversationRight.data},
            {'id': 'сonvention135', 'name': 'Нарушения положений Конвенции МОТ №135', 'item': сonvention135.data},
            {'id': 'consultationRight', 'name': 'Проведение консультаций', 'item': consultationRight.data},
            {'id': 'principleOfNonDiscrimination', 'name': 'Принцип запрещения дискриминации',
            'item': principleOfNonDiscrimination.data},
            {'id': 'discriminatiOnVariousGrounds', 'name': 'Дискриминация по различным основаниям',
            'item': discriminatiOnVariousGrounds.data},
            {'id': 'discriminationInVariousAreas', 'name': 'Дискриминация в различных сферах трудовых отношений',
            'item': discriminationInVariousAreas.data},
            {'id': 'publicPolicyDiscrimination',
             'name': 'Нарушения в области проведения государственной политики по искоренению дискриминации и поощрению равенства прав и возможностей',
            'item': publicPolicyDiscrimination.data},
            {'id': 'childLabor', 'name': 'Дискриминация в различных сферах трудовых отношений',
            'item': childLabor.data},
            {'id': 'сonvention138', 'name': 'О минимальном возрасте для приема на работу', 'item': сonvention138.data},
            {'id': 'convention182',
             'name': 'О запрещении и немедленных мерах по искоренению наихудших форм детского труда',
            'item': convention182.data},
            {'id': 'prohibitionOfForcedLabor', 'name': 'Запрет принудительного труда',
            'item': prohibitionOfForcedLabor.data},
            {'id': 'useOfForcedLabor', 'name': 'Использование принудительного труда', 'item': useOfForcedLabor.data},
            {'id': 'governmentCoercion', 'name': 'Косвенное принуждение государством к труду',
            'item': governmentCoercion.data},
            {'id': 'violationsUsingCompulsoryLabor',
             'name': 'Нарушения при использовании принудительного (обязательного) труда в допустимых случаях',
            'item': violationsUsingCompulsoryLabor.data},
            {'id': 'failureSystemicMeasures', 'name': 'Нарушения, связанные с непринятием государством системных мер',
            'item': failureSystemicMeasures.data},
            {'id': 'victim', 'name': 'В отношении кого совершено нарушение', 'item': victim.data},
            {'id': 'intruder', 'name': 'Кем было совершено нарушение', 'item': intruder.data},
            {'id': 'natureviolation', 'name': 'Характер нарушения', 'item': violation_nature.data},
            {'id': 'rightsstate', 'name': 'Ситуация с правами', 'item': rights_state.data},
            {'id': 'victimsituation', 'name': 'Ситуация с потерпевшим(и)', 'item': victim_situation.data},
            {'id': 'tradeUnionSituation', 'name': 'Профсоюз на месте работы после произошедшего',
            'item': tradeUnionSituation.data},
            {'id': 'user', 'name': 'Монитор', 'item': user.data},
        ])
            # {'tradeUnionCount': {'Численность профсоюза после произошедшего': tradeUnionCount.data}}, #Можно удалить
            # {'company': {'Работодатель(компания)': company.data}}, #Можно удалить
            # {'tradeUnionInfo': {'Профсоюзная организация': tradeUnionInfo.data}}, #Можно удалить
            # {'groupOfPersons': {'Группа лиц (работников)': groupOfPersons.data}}, #Можно удалить


class DataFilterAPI(APIView):
    authentication_classes = []
    def post(self, request):
        my_list = []
        print(request.data)
        for item in request.data:
            if item['id'] == 'user':
                my_list.append(f"auth_user.username")
            else:
                my_list.append(f"work_{item['id']}.name")
        fields = unpucking(my_list)
        # print(my_list)
        case_count = Case.objects.count()
        sql_query = f"SELECT {fields}, count(*), round(count (*) * 100.0 /{case_count}, 2) percent FROM work_case"
        where_query = "where "
        where_list = []
        where_query_list = []
        group_by_query = f"group by {fields}"
        for data in request.data:
            if data['id'] in fields:
                id = data['id']
                item = data['item']
                if id == "country":
                    where_sql_query = "work_case.country_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_country on work_country.id = work_case.country_id "

                elif id == "region":
                    where_sql_query = "work_case.region_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_region on work_region.id = work_case.region_id "

                elif id == "groupofrights":
                    where_sql_query = "work_case.groupofrights_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_groupofrights on work_groupofrights.id = work_case.groupofrights_id "

                elif id == "tradeunionright":
                    where_sql_query = "work_case.tradeunionright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_tradeunionright on work_tradeunionright.id = work_case.tradeunionright_id "

                elif id == "tradeunioncrime":
                    where_sql_query = "work_case.tradeunioncrime_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_tradeunioncrime on work_tradeunioncrime.id = work_case.tradeunioncrime_id "

                elif id == "meetingsright":
                    where_sql_query = "work_case.meetingsright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_meetingsright on work_meetingsright.id = work_case.meetingsright_id "

                elif id == "сonvention87":
                    where_sql_query = "work_case.сonvention87_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_сonvention87 on work_сonvention87.id = work_case.сonvention87_id "

                elif id == "tradeunionbuildingsright":
                    where_sql_query = "work_case.tradeunionbuildingsright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_tradeunionbuildingsright on work_tradeunionbuildingsright.id = work_case.tradeunionbuildingsright_id "

                elif id == "createorganizationright":
                    where_sql_query = "work_case.createorganizationright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_createorganizationright on work_createorganizationright.id = work_case.createorganizationright_id "

                elif id == "createtradeunionright":
                    where_sql_query = "work_case.createtradeunionright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_createtradeunionright on work_createtradeunionright.id = work_case.createtradeunionright_id "

                elif id == "electionsright":
                    where_sql_query = "work_case.electionsright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_electionsright on work_electionsright.id = work_case.electionsright_id "

                elif id == "tradeunionactivityright":
                    where_sql_query = "work_case.tradeunionactivityright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_tradeunionactivityright on work_tradeunionactivityright.id = work_case.tradeunionactivityright_id "

                elif id == "createstrikeright":
                    where_sql_query = "work_case.createstrikeright_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_createstrikeright on work_createstrikeright.id = work_case.createstrikeright_id "

                elif id == "сonvention98":
                    where_sql_query = "work_case.сonvention98_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_сonvention98 on work_сonvention98.id = work_case.сonvention98_id "

                elif id == "antitradeuniondiscrimination":
                    where_sql_query = "work_case.antitradeuniondiscrimination_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_antitradeuniondiscrimination on work_antitradeuniondiscrimination.id = work_case.antitradeuniondiscrimination_id "

                elif id == "сonversationright":
                    where_sql_query = "work_case.conversationRight_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_сonversationright on work_сonversationright.id = work_case.conversationRight_id "

                elif id == "сonvention135":
                    where_sql_query = "work_case.сonvention135_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_сonvention135 on work_сonvention135.id = work_case.сonvention135_id "

                elif id == "consultationright":
                    where_sql_query = "work_case.consultationRight_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_consultationright on work_consultationright.id = work_case.consultationRight_id "

                elif id == "principleofnondiscrimination":
                    where_sql_query = "work_case.principleofnondiscrimination_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_principleofnondiscrimination on work_principleofnondiscrimination.id = work_case.principleofnondiscrimination_id "

                elif id == "discriminationvariousgrounds":
                    where_sql_query = "work_case.discriminationvariousgrounds_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_discriminationvariousgrounds on work_discriminationvariousgrounds.id = work_case.discriminationvariousgrounds_id "

                elif id == "discriminationinvariousareas":
                    where_sql_query = "work_case.discriminationinvariousareas_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_discriminationinvariousareas on work_discriminationinvariousareas.id = work_case.discriminationinvariousareas_id "

                elif id == "publicpolicydiscrimination":
                    where_sql_query = "work_case.publicpolicydiscrimination_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_publicpolicydiscrimination on work_publicpolicydiscrimination.id = work_case.publicpolicydiscrimination_id "

                elif id == "childlabor":
                    where_sql_query = "work_case.childlabor_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_childlabor on work_childlabor.id = work_case.childlabor_id "

                elif id == "сonvention138":
                    where_sql_query = "work_case.сonvention138_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_сonvention138 on work_сonvention138.id = work_case.сonvention138_id "

                elif id == "convention182":
                    where_sql_query = "work_case.convention182_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_convention182 on work_convention182.id = work_case.convention182_id "

                elif id == "prohibitionofforcedlabor":
                    where_sql_query = "work_case.prohibitionofforcedlabor_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_prohibitionofforcedlabor on work_prohibitionofforcedlabor.id = work_case.prohibitionofforcedlabor_id "

                elif id == "useofforcedlabor":
                    where_sql_query = "work_case.useofforcedlabor_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_useofforcedlabor on work_useofforcedlabor.id = work_case.useofforcedlabor_id "

                elif id == "governmentcoercion":
                    where_sql_query = "work_case.governmentcoercion_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_governmentcoercion on work_governmentcoercion.id = work_case.governmentcoercion_id "

                elif id == "violationsusingcompulsorylabor":
                    where_sql_query = "work_case.violationsusingcompulsorylabor_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_violationsusingcompulsorylabor on work_violationsusingcompulsorylabor.id = work_case.violationsusingcompulsorylabor_id "

                elif id == "failuresystemicmeasures":
                    where_sql_query = "work_case.failuresystemicmeasures_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_failuresystemicmeasures on work_failuresystemicmeasures.id = work_case.failuresystemicmeasures_id "

                elif id == "victim":
                    where_sql_query = "work_case.victim_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_victim on work_victim.id = work_case.victim_id "

                elif id == "natureviolation":
                    where_sql_query = "work_case.violation_nature_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_natureviolation on work_natureviolation.id = work_case.violation_nature_id "

                elif id == "rightsstate":
                    where_sql_query = "work_case.rights_state_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_rightsstate on work_rightsstate.id = work_case.rights_state_id "

                elif id == "victimsituation":
                    where_sql_query = "work_case.victim_situation_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_victimsituation on work_victimsituation.id = work_case.victim_situation_id "

                elif id == "tradeunionsituation":
                    where_sql_query = "work_case.tradeunionsituation_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_tradeunionsituation on work_tradeunionsituation.id = work_case.tradeunionsituation_id "

                elif id == "user":
                    where_sql_query = "work_case.user_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join auth_user on auth_user.id = work_case.user_id "


                # elif id == "": # Экземпляр
                #     where_sql_query = "work_case._id in "
                #     for i in item:
                #         where_list.append(i['id'])
                #     if len(where_list) > 1:
                #         where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                #     else:
                #         where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                #     where_list.clear()
                #     sql_query += " join work_ on work_.id = work_case._id "


                # Ниже представлены ManyToMany связи!
                elif id == "source":
                    where_sql_query = "work_case_source.source_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_case_source on work_case.id = work_case_source.case_id join work_source on work_case_source.source_id = work_source.id "
                elif id == "intruder":
                    where_sql_query = "work_case_intruder.intruder_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join work_case_intruder on work_case.id = work_case_intruder.case_id join work_intruder on work_case_intruder.intruder_id = work_intruder.id "
            else:
                continue
        where_query_list = 'and '.join(where_query_list)
        where_query += where_query_list
        # print(where_query)
        print(sql_query + where_query + group_by_query)
        with connection.cursor() as cursor:
            cursor.execute(sql_query + where_query + group_by_query)
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
        return Response(response_list)
