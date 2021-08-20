import os
from io import BytesIO, StringIO

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from xhtml2pdf import pisa
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import CaseForm, CompanyForm, IndividualForm, GroupForm, EntrepreneurForm, PhotoForm, FileForm, CaseCommentForm
from .filters import MigrantFilter
from .serializers import *
# Create your views here.
from .models import *
from main.service import unpucking
from django.db import connection
from django.http import Http404
from django.utils.decorators import method_decorator
from docxtpl import DocxTemplate
import jinja2
from .templatetags.migrant_tags import var_verbose_name_for_word, check_arg_is_none
import pdfkit


@login_required
def append_case(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)
        photoForm = PhotoForm(request.POST, request.FILES)
        fileForm = FileForm(request.POST, request.FILES)

        if form.is_valid():

            # cleaned_data = form.cleaned_data;
            # if request.user.is_authenticated():
            #     form.instance.user = request.user
            # if cleaned_data['source']:
            #     for item in cleaned_data['source']:
            #         if item.id == 5:
            #             pass
            case = form.save(commit=False)


            if companyForm.is_valid():
                case.company = companyForm.save()
            if individualForm.is_valid():
                case.individualInfo = individualForm.save()
            # if victimForm.is_valid():
            #     victim = victimForm.save(commit=False)
            #     case.victim = victim
            #     victim.save()
            if groupForm.is_valid():
                case.personGroupInfo = groupForm.save()
            if entrepreneurForm.is_valid():
                case.entrepreneur = entrepreneurForm.save()

            case.user = request.user
            case.save()
            form._save_m2m()

            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CasePhoto(photo=f, card=case)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CaseFile(file=f, card=case)
                    file.save()

            return redirect('migrants_list')

    else:
        form = CaseForm
        companyForm = CompanyForm
        individualForm = IndividualForm
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
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                      'photoForm': photoForm,
                      'fileForm': fileForm,
                  })
@login_required()
def delete_case(request, pk):
    case = Case.objects.get(id=pk).delete()
    return redirect('migrants_list')

@login_required()
def update_case(request,pk):
    case = Case.objects.get(id=pk)

    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)
        photoForm = PhotoForm(request.POST, request.FILES)
        fileForm = FileForm(request.POST, request.FILES)

        if form.is_valid():
            form.save(commit=False)

        if companyForm.is_valid():
            case.company = companyForm.save()
        if individualForm.is_valid():
            case.individualInfo = individualForm.save()
        if groupForm.is_valid():
            case.personGroupInfo = groupForm.save()
        if entrepreneurForm.is_valid():
            case.entrepreneur = entrepreneurForm.save()

        case.user = request.user
        case.save()
        form._save_m2m()

        if photoForm.is_valid():
            for f in request.FILES.getlist('photo'):
                photo = CasePhoto(photo=f, card=case)
                photo.save()
        if fileForm.is_valid():
            for f in request.FILES.getlist('file'):
                file = CaseFile(file=f, card=case)
                file.save()

        return redirect('migrants_list')
    else:
        form = CaseForm(instance=case)

        companyForm = CompanyForm()
        if case.company is not None:
            companyForm = CompanyForm(instance=Company.objects.get(id=case.company))

        individualForm = IndividualForm
        if case.individualInfo is not None:
            individualForm = IndividualForm(instance=IndividualInfo.objects.get(id = case.individualInfo_id))

        # victimForm = VictimForm
        # if case.victim is not None:
        #     victimForm = VictimForm(instance=Victim.objects.get(id=case.victim_id))

        groupForm = GroupForm()
        if case.personGroupInfo is not None:
            groupForm = GroupForm(instance=PersonGroup.objects.get(id = case.personGroupInfo_id))

        entrepreneurForm = EntrepreneurForm
        if case.entrepreneur is not None:
            entrepreneurForm = EntrepreneurForm(instance = Entrepreneur.objects.get(id = case.entrepreneur_id))
        #
        # photos = CasePhoto.objects.get(card = case.id)
        # print(photos)
        photoForm = PhotoForm
        fileForm = FileForm

    return render(request,
                  'migrant/add_case.html',
                  context={
                      'form': form,
                      'companyForm': companyForm,
                      'individualForm': individualForm,
                      # 'victimForm': victimForm,
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                      'photoForm': photoForm,
                      'fileForm': fileForm,
                  })

@login_required()
def cases(request):
    if request.user.position.role_id == 1:
        cases = Case.objects.all()
        filter = MigrantFilter(request.GET, queryset=cases)
        cards = filter.qs
        context = {'cards': cards, 'myFilter': filter}
        return render(request, 'migrant/cases.html', context)
    elif request.user.position.role_id == 2 or request.user.position.role_id == 3:
        cases = Case.objects.filter(country_id=request.user.country.country_id)
        filter = MigrantFilter(request.GET, queryset=cases)
        cards = filter.qs
        context = {'cards': cards, 'myFilter': filter}
        return render(request, 'migrant/cases.html', context)
    else:
        raise Http404('Недостаточно прав!')

def multistep(request):
    return render(request, 'migrant/add_case.html')


def download(request, case_id):
    pass


def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id)
    return render(request,'migrant/region_dropdown.html',{'regions':regions})

@login_required()
def add_comment(request, pk):
    case = Case.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data['case'] = case.id
        form = CaseCommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('migrants_list')
    else:
        form = CaseCommentForm()
    return render(request, 'migrant/add_comment.html', {'form': form, 'case': case})


def show_comments(request, pk):
    comments = CaseComment.objects.filter(case_id=pk, active=True)
    return render(request, 'migrant/show_comments.html', {'comments': comments})


def delete_comment(request, pk):
    CaseComment.objects.get(id=pk).delete()
    return redirect('migrants_list')


def case_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    case = get_object_or_404(Case, pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    right = Right.objects.filter(case__pk=pk)
    intruder = Intruder.objects.filter(case__pk=pk)
    comments = CaseComment.objects.filter(case_id=pk)
    template_path = 'migrant/migrant_pdf.html'
    context = {
        'case': case,
        'source': source,
        'right': right,
        'intruder': intruder,
        'comments': comments,
    }
    # Create a Django response object, and specify content_type as pdf
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # print(html)
    # create a pdf
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename="document.pdf"'
    # if error then show some funy view
    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def case_download_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    case = get_object_or_404(Case, pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    right = Right.objects.filter(case__pk=pk)
    intruder = Intruder.objects.filter(case__pk=pk)
    comments = CaseComment.objects.filter(case_id=pk)
    template_path = 'migrant/migrant_pdf.html'
    context = {
        'case': case,
        'source': source,
        'right': right,
        'intruder': intruder,
        'comments': comments,
    }
    # Create a Django response object, and specify content_type as pdf
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # print(html)
    # create a pdf
    pdf = pdfkit.from_string(html, False)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="document.pdf"'
    # if error then show some funy view
    # if pisa_status.err:
    #     return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def test(request, pk):
    case = Case.objects.get(pk=pk)
    photos = CasePhoto.objects.filter(card_id=pk)
    print(photos)
    for i in photos:
        print(i)
    return render(request, 'migrant/migrant_pdf.html', {'case': case, 'photos': photos})


class DataAPIView(APIView):
    def get(self, request):
        country = CountrySerializers(Country.objects.all(), many=True)
        region_1 = RegionSerializers(Region.objects.filter(country__pk=1), many=True)
        region_2 = RegionSerializers(Region.objects.filter(country__pk=2), many=True)
        region_3 = RegionSerializers(Region.objects.filter(country__pk=3), many=True)
        region_4 = RegionSerializers(Region.objects.filter(country__pk=4), many=True)
        region_5 = RegionSerializers(Region.objects.filter(country__pk=5), many=True)
        victim = VictimSerializers(Victim.objects.all(), many=True)
        banOnEntry = BanOnEntrySerializers(BanOnEntry.objects.all(), many=True)
        source = InfoSourceSerializers(InfoSource.objects.all(), many=True)
        violated_right = RightSerializers(Right.objects.all(), many=True)
        victim = VictimSerializers(Victim.objects.all(), many=True)
        # individualInfo = IndividualInfoSerializers(IndividualInfo.objects.all(), many=True)
        intruder = IntruderSerializers(Intruder.objects.all(), many=True)
        violation_nature = NatureViolationSerializers(NatureViolation.objects.all(), many=True)
        # personGroupInfo = PersonGroupSerializers(PersonGroup.objects.all(), many=True)
        entrepreneur = EntrepreneurSerializers(Entrepreneur.objects.all(), many=True)
        rights_state = RightsStateSerializers(RightsState.objects.all(), many=True)
        victim_situation = VictimSituationSerializers(VictimSituation.objects.all(), many=True)
        tradeUnionSituation = TradeUnionSituationSerializers(TradeUnionSituation.objects.all(), many=True)
        violationType = ViolationTypeSerializers(ViolationType.objects.all(), many=True)
        changesInSalary = ChangesInSalarySerializers(ChangesInSalary.objects.all(), many=True)
        user = UserSerializers(User.objects.all(), many=True)
        # company = CompanySerializers(Company.objects.all(), many=True)
        # tradeUnionCount = TradeUnionCountSerializers(TradeUnionCount.objects.all(), many=True)
        return Response([
            {'id': 'country', 'name': 'Страна', 'item': country.data},
            {'id': 'region', 'name': 'Регион', 'item': {1: region_1.data,
                                                        2: region_2.data,
                                                        3: region_3.data,
                                                        4: region_4.data,
                                                        5: region_5.data}},
            {'id': 'victim', 'name': 'В отношении кого совершено нарушение', 'item': victim.data},
            {'id': 'banonentry', 'name': 'Есть ли у вас запрет на въезд?', 'item': banOnEntry.data},
            {'id': 'infosource', 'name': 'Источник информации о нарушении', 'item': source.data},
            {'id': 'right', 'name': 'Какое право нарушено?', 'item': violated_right.data},
            # {'id': 'individualinfo', 'name': 'физическое лицо', 'item': individualInfo.data}, #50 % 50
            # {'id': 'personGroupInfo', 'name': 'Группа лиц', 'item': personGroupInfo.data},
            {'id': 'entrepreneur', 'name': 'Работодатель(Частное лицо)', 'item': entrepreneur.data},
            {'id': 'intruder', 'name': 'Кем было совершено нарушение', 'item': intruder.data},
            {'id': 'natureviolation', 'name': 'Характер нарушения', 'item': violation_nature.data},
            {'id': 'rightsstate', 'name': 'Ситуация с правами', 'item': rights_state.data},
            {'id': 'victimsituation', 'name': 'Ситуация с потерпевшим(и)', 'item': victim_situation.data},
            {'id': 'tradeunionsituation', 'name': 'Профсоюз на месте работы после произошедшего',
             'item': tradeUnionSituation.data},
            {'id': 'violationtype', 'name': 'С какими нарушениями трудовых прав вы столкнулись из-за COVID-19?',
             'item': violationType.data},
            {'id': 'changesinsalary', 'name': 'Как изменились Ваши доходы из-за COVID-19?', 'item': changesInSalary.data},
            {'id': 'user', 'name': 'Монитор', 'item': user.data},
        ])
        # {'id': 'company', 'name': 'Работодатель(компания)', 'item': company.data},  # Можно удалить
        # {'id': 'tradeUnionCount', 'name': 'Численность профсоюза после произошедшего',
        #  'item': tradeUnionCount.data},  # Можно удалить

class DataFilterAPI(APIView):
    authentication_classes = []
    def post(self, request):
        my_list = []
        print(request.data)
        for item in request.data:
            if item['id'] == 'user':
                my_list.append(f"auth_user.username")
            elif item['id'] == 'entrepreneur':
                my_list.append(f"migrant_entrepreneur.entrepreneur_name")
            else:
                my_list.append(f"migrant_{item['id']}.name")
        fields = unpucking(my_list)
        # print(my_list)
        case_count = Case.objects.count()
        sql_query = f"SELECT {fields}, count(*), count(*), 100 / count (*) FROM migrant_case"
        where_query = "where "
        where_list = []
        where_query_list = []
        group_by_query = f"group by {fields}"
        for data in request.data:
            if data['id'] in fields:
                id = data['id']
                item = data['item']
                if id == "country":
                    where_sql_query = "migrant_case.country_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_country on migrant_country.id = migrant_case.country_id "

                elif id == "region":
                    where_sql_query = "migrant_case.region_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_region on migrant_region.id = migrant_case.region_id "

                elif id == "banonentry":
                    where_sql_query = "migrant_case.banonentry_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_banonentry on migrant_banonentry.id = migrant_case.banonentry_id "

                elif id == "individualinfo":
                    where_sql_query = "migrant_case.individualinfo_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_individualinfo on migrant_individualinfo.id = migrant_case.individualinfo_id "

                elif id == "entrepreneur":
                    where_sql_query = "migrant_case.entrepreneur_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_entrepreneur on migrant_entrepreneur.id = migrant_case.entrepreneur_id "

                elif id == "violationtype":
                    where_sql_query = "migrant_case.violationtype_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_violationtype on migrant_violationtype.id = migrant_case.violationtype_id "

                elif id == "changesinsalary":
                    where_sql_query = "migrant_case.changesinsalary_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_changesinsalary on migrant_changesinsalary.id = migrant_case.changesinsalary_id "

                elif id == "victim":
                    where_sql_query = "migrant_case.victim_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_victim on migrant_victim.id = migrant_case.victim_id "

                elif id == "natureviolation":
                    where_sql_query = "migrant_case.violation_nature_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_natureviolation on migrant_natureviolation.id = migrant_case.violation_nature_id "

                elif id == "rightsstate":
                    where_sql_query = "migrant_case.rights_state_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_rightsstate on migrant_rightsstate.id = migrant_case.rights_state_id "

                elif id == "victimsituation":
                    where_sql_query = "migrant_case.victim_situation_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_victimsituation on migrant_victimsituation.id = migrant_case.victim_situation_id "

                elif id == "tradeunionsituation":
                    where_sql_query = "migrant_case.tradeunionsituation_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_tradeunionsituation on migrant_tradeunionsituation.id = migrant_case.tradeunionsituation_id "

                elif id == "user":
                    where_sql_query = "migrant_case.user_id in "
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join auth_user on auth_user.id = migrant_case.user_id "


                # elif id == "": # Экземпляр
                #     where_sql_query = "migrant_case._id in "
                #     for i in item:
                #         where_list.append(i['id'])
                #     if len(where_list) > 1:
                #         where_query_list.append(f"{where_sql_query} {tuple(where_list)}")
                #     else:
                #         where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                #     where_list.clear()
                #     sql_query += " join migrant_ on migrant_.id = migrant_case._id "


                # Ниже представлены ManyToMany связи!
                elif id == "infosource":
                    where_sql_query = "migrant_case_source.infosource_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_case_source on migrant_case.id = migrant_case_source.case_id join migrant_infosource on migrant_case_source.infosource_id = migrant_infosource.id "

                elif id == "intruder":
                    where_sql_query = "migrant_case_intruder.intruder_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_case_intruder on migrant_case.id = migrant_case_intruder.case_id join migrant_intruder on migrant_case_intruder.intruder_id = migrant_intruder.id "

                elif id == "right":
                    where_sql_query = "migrant_case_violated_right.right_id in"
                    for i in item:
                        where_list.append(i['id'])
                    if len(where_list) > 1:
                        where_query_list.append(f"{where_sql_query} {tuple(where_list)} ")
                    else:
                        where_query_list.append(f"{where_sql_query} ({where_list[0]}) ")
                    where_list.clear()
                    sql_query += " join migrant_case_violated_right on migrant_case.id = migrant_case_violated_right.case_id join migrant_right on migrant_case_violated_right.right_id = migrant_right.id "
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
            for i in range(len(response_list)):
                response_list[i]['percent'] = 100 / len(response_list)
        return Response(response_list)


def case_files_download(request, pk):
    if request.user.position.role_id == 3:
        case = Case.objects.get(user=request.user, pk=pk)
        images = CasePhoto.objects.filter(card_id=case.id)
        files = CaseFile.objects.filter(card_id=case.id)
        return render(request, 'migrant/files_download.html', {'images': images, 'files': files})
    else:
        case = Case.objects.get(pk=pk)
        images = CasePhoto.objects.filter(card_id=case.id)
        files = CaseFile.objects.filter(card_id=case.id)
        return render(request, 'migrant/files_download.html', {'images': images, 'files': files})


def generate_case_word(request, pk):
    case = Case.objects.get(pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    right = Right.objects.filter(case__pk=pk)
    intruder = Intruder.objects.filter(case__pk=pk)
    comments = CaseComment.objects.filter(case_id=pk)
    base_dir = str(settings.BASE_DIR)
    base_dir += "/migrant/static/word/migrant/"
    tpl = DocxTemplate(base_dir + 'template.docx')
    context = {
        'case': case,
        'source': source,
        'right': right,
        'intruder': intruder,
        'comments': comments
    }
    jinja_env = jinja2.Environment()
    jinja_env.filters['var_verbose_name'] = var_verbose_name_for_word
    jinja_env.filters['check_arg_is_none'] = check_arg_is_none
    tpl.render(context, jinja_env=jinja_env)
    save_path = base_dir + 'document.docx'
    tpl.save(save_path)
    if os.path.exists(save_path):
        with open(save_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-word")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(save_path)
            return response
    return Http404()


from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def get_fields_name(model, field):
    try:
        return model._meta.get_field(field).verbose_name
    except Exception:
        return 'Error'

def pdf_table_download(request, *args, **kwargs):
    pk = kwargs.get('pk')
    case = get_object_or_404(Case, pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    source_len = len(source)
    right = Right.objects.filter(case__pk=pk)
    right_len = len(right)
    intruder = Intruder.objects.filter(case__pk=pk)
    intruder_len = len(intruder)
    comments = CaseComment.objects.filter(case_id=pk)
    comments_len = len(comments)
    # Create the HttpResponse object
    response = HttpResponse(content_type='application/pdf')
    # This line force a download
    response['Content-Disposition'] = 'attachment; filename="1.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Black.ttf'))

    data = [[get_fields_name(Case, 'case_name'), case.case_name],
            [get_fields_name(Case, 'country'), case.country],
            [get_fields_name(Case, 'region'), case.region],
            [get_fields_name(Case, 'date_create'), case.date_create.strftime('%Y-%m-%d %H:%M:%S')],
            [get_fields_name(Case, 'date_update'), case.date_update.strftime('%Y-%m-%d %H:%M:%S')],
            [get_fields_name(Case, 'victim_status'), case.victim_status],
            [get_fields_name(Case, 'banOnEntry'), case.banOnEntry],
            [get_fields_name(Case, 'banned_country'), case.banned_country],
            [get_fields_name(Case, 'banOnEntryAnother'), case.banOnEntryAnother],
            [get_fields_name(Case, 'case_date'), case.case_date],
            [get_fields_name(Case, 'start_date'), case.start_date],
            [get_fields_name(Case, 'end_date'), case.end_date],
            [get_fields_name(Case, 'victim'), case.victim],
            [get_fields_name(Case, 'victim_situation'), case.victim_situation],
            [get_fields_name(Case, 'victim_situation_another'), case.victim_situation_another],
            [get_fields_name(Case, 'individualInfo'), case.individualInfo],
            [get_fields_name(Case, 'personGroupInfo'), case.personGroupInfo],
            [get_fields_name(Case, 'government_agency_name'), case.government_agency_name],
            [get_fields_name(Case, 'local_agency_name'), case.local_agency_name],
            [get_fields_name(Case, 'police_agency_name'), case.police_agency_name],
            [get_fields_name(Case, 'control_agency_name'), case.control_agency_name],
            [get_fields_name(Case, 'company'), case.company],
            [get_fields_name(Case, 'entrepreneur'), case.entrepreneur],
            [get_fields_name(Case, 'case_additional'), case.case_additional[0:48]],
            [get_fields_name(Case, 'story')[0:48], case.story[0:48]],
            [get_fields_name(Case, 'actions')[0:48], case.actions[0:48]],
            [get_fields_name(Case, 'final')[0:48], case.final[0:48]],
            [get_fields_name(Case, 'violation_nature'), case.violation_nature],
            [get_fields_name(Case, 'rights_state'), case.rights_state],
            [get_fields_name(Case, 'rights_state_another'), case.rights_state_another],
            [get_fields_name(Case, 'tradeUnionSituation'), case.tradeUnionSituation],
            [get_fields_name(Case, 'tradeUnionSituation_another'), case.tradeUnionSituation_another],
            [get_fields_name(Case, 'tradeUnionCount'), case.tradeUnionCount],
            [get_fields_name(Case, 'case_additional_info'), case.case_additional_info],
            [get_fields_name(Case, 'frequent_problems')[0:48], case.frequent_problems],
            [get_fields_name(Case, 'decision')[0:48], case.decision],
            [get_fields_name(Case, 'advice')[0:48], case.advice],

            [get_fields_name(Case, 'has_violation_in_covid')[0:48], case.has_violation_in_covid],
            [get_fields_name(Case, 'violationType')[0:48], case.violationType],
            [get_fields_name(Case, 'violationType_another')[0:48], case.violationType_another],
            [get_fields_name(Case, 'changesInSalary')[0:48], case.changesInSalary],
            [get_fields_name(Case, 'changesInSalary_another')[0:48], case.changesInSalary_another],
            [get_fields_name(Case, 'user'), case.user],
            ]
    for i in range(source_len):
        data.append([get_fields_name(Case, 'source'), source[i].name])
    data.append([get_fields_name(Case, 'source_url'), case.source_url])
    data.append([get_fields_name(Case, 'source_content')[0:48], case.source_content[0:48]])
    for i in range(right_len):
        data.append([get_fields_name(Case, 'violated_right'), right[i].name])
    data.append([get_fields_name(Case, 'violatedRightAnother'), case.violatedRightAnother])
    for i in range(intruder_len):
        data.append([get_fields_name(Case, 'intruder'), intruder[i].name])
    for i in range(comments_len):
        data.append([get_fields_name(Case, 'comment'), comments[i].comment])
    t = Table(data)

    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.white),
                           ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                           ('FONTNAME', (0, 0), (-1, -1), 'Roboto')]))
    elements.append(t)
    # write the document to disk
    doc.build(elements)

    return response

def pdf_table_generate(request, *args, **kwargs):
    pk = kwargs.get('pk')
    case = get_object_or_404(Case, pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    source_len = len(source)
    right = Right.objects.filter(case__pk=pk)
    right_len = len(right)
    intruder = Intruder.objects.filter(case__pk=pk)
    intruder_len = len(intruder)
    comments = CaseComment.objects.filter(case_id=pk)
    comments_len = len(comments)
    # Create the HttpResponse object
    response = HttpResponse(content_type='application/pdf')
    # This line force a download
    response['Content-Disposition'] = 'filename="1.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    # container for the 'Flowable' objects
    elements = []
    pdfmetrics.registerFont(TTFont('Roboto', 'Roboto-Black.ttf'))
    data = [[get_fields_name(Case, 'case_name'), case.case_name],
            [get_fields_name(Case, 'country'), case.country],
            [get_fields_name(Case, 'region'), case.region],
            [get_fields_name(Case, 'date_create'), case.date_create.strftime('%Y-%m-%d %H:%M:%S')],
            [get_fields_name(Case, 'date_update'), case.date_update.strftime('%Y-%m-%d %H:%M:%S')],
            [get_fields_name(Case, 'victim_status'), case.victim_status],
            # [get_fields_name(Case, 'banOnEntry'), case.banOnEntry],
            # [get_fields_name(Case, 'banned_country'), case.banned_country],
            # [get_fields_name(Case, 'banOnEntryAnother'), case.banOnEntryAnother],
            # [get_fields_name(Case, 'case_date'), case.case_date],
            # [get_fields_name(Case, 'start_date'), case.start_date],
            # [get_fields_name(Case, 'end_date'), case.end_date],
            # [get_fields_name(Case, 'victim'), case.victim],
            # [get_fields_name(Case, 'victim_situation'), case.victim_situation],
            # [get_fields_name(Case, 'victim_situation_another'), case.victim_situation_another],
            # [get_fields_name(Case, 'individualInfo'), case.individualInfo],
            # [get_fields_name(Case, 'personGroupInfo'), case.personGroupInfo],
            # [get_fields_name(Case, 'government_agency_name'), case.government_agency_name],
            # [get_fields_name(Case, 'local_agency_name'), case.local_agency_name],
            # [get_fields_name(Case, 'police_agency_name'), case.police_agency_name],
            # [get_fields_name(Case, 'control_agency_name'), case.control_agency_name],
            # [get_fields_name(Case, 'company'), case.company],
            # [get_fields_name(Case, 'entrepreneur'), case.entrepreneur],
            # [get_fields_name(Case, 'case_additional'), case.case_additional[0:48]],
            # [get_fields_name(Case, 'story')[0:48]+'\n'+get_fields_name(Case, 'story')[48:96]+'\n'+get_fields_name(Case, 'story')[96:130]+'\n'+get_fields_name(Case, 'story')[130:], case.story[0:48]],
            # [get_fields_name(Case, 'actions')[0:48], case.actions[0:48]],
            # [get_fields_name(Case, 'final')[0:48], case.final[0:48]],
            # [get_fields_name(Case, 'violation_nature'), case.violation_nature],
            # [get_fields_name(Case, 'rights_state'), case.rights_state],
            # [get_fields_name(Case, 'rights_state_another'), case.rights_state_another],
            # [get_fields_name(Case, 'tradeUnionSituation'), case.tradeUnionSituation],
            # [get_fields_name(Case, 'tradeUnionSituation_another'), case.tradeUnionSituation_another],
            # [get_fields_name(Case, 'tradeUnionCount'), case.tradeUnionCount],
            # [get_fields_name(Case, 'case_additional_info'), case.case_additional_info],
            # [get_fields_name(Case, 'frequent_problems')[0:48], case.frequent_problems],
            # [get_fields_name(Case, 'decision')[0:48], case.decision],
            # [get_fields_name(Case, 'advice')[0:48], case.advice],
            # [get_fields_name(Case, 'has_violation_in_covid')[0:48], case.has_violation_in_covid],
            # [get_fields_name(Case, 'violationType')[0:48], case.violationType],
            # [get_fields_name(Case, 'violationType_another')[0:48], case.violationType_another],
            # [get_fields_name(Case, 'changesInSalary')[0:48], case.changesInSalary],
            # [get_fields_name(Case, 'changesInSalary_another')[0:48]+'\n'+get_fields_name(Case, 'changesInSalary_another')[48::], case.changesInSalary_another],
            # [get_fields_name(Case, 'user'), case.user],
            ['Какая помощь на ваш взгляд необходима мигрантам?\nКакая помощь на ваш взгляд необходима мигрантам?',
             'Какая помощь на ваш взгляд необходима мигрантам?']
            ]
    for i in range(source_len):
        data.append([get_fields_name(Case, 'source'), source[i].name])

    data.append([get_fields_name(Case, 'source_url'), case.source_url])
    data.append([get_fields_name(Case, 'source_content')[0:48], case.source_content[0:48]])
    for i in range(right_len):
        data.append([get_fields_name(Case, 'violated_right'), right[i].name])
    data.append([get_fields_name(Case, 'violatedRightAnother'), case.violatedRightAnother])
    for i in range(intruder_len):
        data.append([get_fields_name(Case, 'intruder'), intruder[i].name])
    for i in range(comments_len):
        data.append([get_fields_name(Case, 'comment'), comments[i].comment])
    t = Table(data)

    t.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, -1), colors.white),
                           ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
                           ('FONTNAME', (0, 0), (-1, -1), 'Roboto')]))
    elements.append(t)
    # write the document to disk
    doc.build(elements)

    return response