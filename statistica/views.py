from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import generics
from django.shortcuts import get_object_or_404, render
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

# Create your views here.
from migrant.models import Case as MigrantCase, InfoSource, Right, CaseComment as MigrantCaseComment, Intruder as MigrantIntruder
from work.models import Case as WorkCase, Source, Intruder, TradeUnionActivities, CaseComment, Case
from strike.models import Card, DemandCategory, EconomicDemand, PoliticDemand, ComboDemand, CardComment, Source as StrikeSource
from statistica.serializers import WorkResultSerializer, MigrantResultSerializer, StrikeResultSerializer




class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return



@login_required()
def home(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        scheme = request.scheme
        url = request.META.get("HTTP_HOST")
        return render(request, 'statistica/home.html', {'url': f'{scheme}://{url}'})
    else:
        raise Http404('Недостаточно прав!')


@login_required()
def migrant_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        scheme = request.scheme
        url = request.META.get("HTTP_HOST")
        return render(request, 'statistica/migrant_search.html', {'url': f'{scheme}://{url}'})
    else:
        raise Http404('Недостаточно прав!')


@login_required()
def strike_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        scheme = request.scheme
        url = request.META.get("HTTP_HOST")
        return render(request, 'statistica/strike_search.html', {'url': f'{scheme}://{url}'})
    else:
        raise Http404('Недостаточно прав!')


@login_required()
def work_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        scheme = request.scheme
        url = request.META.get("HTTP_HOST")
        return render(request, 'statistica/work_search.html', {'url': f'{scheme}://{url}'})
    else:
        raise Http404('Недостаточно прав!')


class MigrantResultApiView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        filters = dict(request.data)
        list_filter = list(filters.keys())
        intruder_id = filters.get('intruder_id')
        violated_right_id = filters.get('violated_right_id')
        source_id = filters.get('source_id')


        if "intruder_id" in list_filter:
            filters["intruder__in"] = [intruder_id]
            filters.pop("intruder_id")
        if "violated_right_id" in list_filter:
            filters["violated_right__in"] = [violated_right_id]
            filters.pop("violated_right_id")
        if "source_id" in list_filter:
            filters["source__in"] = [source_id]
            filters.pop("source_id")
        print(filters)
        cases = MigrantCase.objects.filter(**filters).order_by('id')
        serializer = MigrantResultSerializer(cases, many=True)
        return Response(serializer.data)



class WorkResultApiView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        filters = dict(request.data)
        list_filter = list(filters.keys())
        intruder_id = filters.get('intruder_id')
        source_id = filters.get('source_id')
        groupofrights_id = filters.get('groupofrights_id')
        tradeunionright_id = filters.get('tradeunionright_id')
        tradeunioncrime_id = filters.get('tradeunioncrime_id')

        if "intruder_id" in list_filter:
            filters["intruder__in"] = [intruder_id]
            filters.pop("intruder_id")

        if "source_id" in list_filter:
            filters["source__in"] = [source_id]
            filters.pop("source_id")

        if "groupofrights_id" in list_filter:
            filters["groupOfRights__in"] = [groupofrights_id]
            filters.pop("groupofrights_id")

        if "tradeunionright_id" in list_filter:
            filters["tradeUnionRight__in"] = [tradeunionright_id]
            filters.pop("tradeunionright_id")

        # if "tradeunioncrime_id" in list_filter:
        #     filters["tradeUnionCrime__in"] = [tradeunioncrime_id]
        #     filters.pop("tradeunioncrime_id")

        print(filters, 'filters')
        workcases = WorkCase.objects.filter(**filters).order_by('id')
        serializer = WorkResultSerializer(workcases, many=True)
        return Response(serializer.data)


class StrikeResultApiView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request):
        filters = dict(request.data)
        card_sources_id = filters.get("card_sources_id")
        card_demand_categories_id = filters.get("card_demand_categories_id")
        economic_demands_id = filters.get("economic_demands_id")
        politic_demands_id = filters.get("politic_demands_id")
        combo_demands_id = filters.get("combo_demands_id")
        list_filter = list(filters.keys())

        if "card_demand_categories_id" in list_filter:
            filters["card_demand_categories__in"] = [card_demand_categories_id]
            filters.pop("card_demand_categories_id")
        if "economic_demands_id" in list_filter:
            filters["economic_demands__in"] = [economic_demands_id]
            filters.pop("economic_demands_id")
        if "politic_demands_id" in list_filter:
            filters["politic_demands__in"] = [politic_demands_id]
            filters.pop("politic_demands_id")
        if "combo_demands_id" in list_filter:
            filters["combo_demands__in"] = [combo_demands_id]
            filters.pop("combo_demands_id")
        if "card_sources_id" in list_filter:
            filters["card_sources__in"] = [card_sources_id]
            filters.pop("card_sources_id")


        # cases = Card.objects.all()

        cards = Card.objects.filter(**filters).order_by('id')
        serializer = StrikeResultSerializer(cards, many=True)
        return Response(serializer.data)


def case_detail(request, pk):
    case = get_object_or_404(Case, pk=pk)
    source = Source.objects.filter(case__pk=pk)
    intruder = Intruder.objects.filter(case__pk=pk)
    trade_union_activities = TradeUnionActivities.objects.filter(case__id=pk)
    comments = CaseComment.objects.filter(case_id=pk)
    return render(request, 'statistica/detail_case.html', locals())


def card_strike_detail(request, pk):
    card = get_object_or_404(Card, id=pk)
    card_sources = StrikeSource.objects.filter(source__pk=pk)
    card_demand_categories = DemandCategory.objects.filter(card__pk=pk)
    economic_demands = EconomicDemand.objects.filter(card__pk=pk)
    politic_demands = PoliticDemand.objects.filter(card__pk=pk)
    combo_demands = ComboDemand.objects.filter(card__pk=pk)
    comments = CardComment.objects.filter(card_id=pk)

    return render(request, 'statistica/detail_card_strike.html', locals())


def case_migrant_detail(request, pk):
    case = get_object_or_404(MigrantCase, pk=pk)
    source = InfoSource.objects.filter(case__pk=pk)
    right = Right.objects.filter(case__pk=pk)
    intruder = MigrantIntruder.objects.filter(case__pk=pk)
    comments = MigrantCaseComment.objects.filter(case_id=pk)
    return render(request, 'statistica/detail_migrant.html', locals())

