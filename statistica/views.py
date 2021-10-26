from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
from migrant.models import Case as MigrantCase
from work.models import Case as WorkCase
from strike.models import Card
from statistica.serializers import WorkResultSerializer, MigrantResultSerializer, StrikeResultSerializer



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



class MigrantResulApiView(APIView):
    def post(self, request):
        filters = request.data
        cases = MigrantCase.objects.filter(**filters)
        serializer = ResultSerializer(cases, many=True)
        return Response({"cases": serializer.data})

class MigrantResultApiView(APIView):

    def post(self, request):
        filters = request.data
        cases = MigrantCase.objects.filter(**filters)
        serializer = MigrantResultSerializer(cases, many=True)
        return Response({"cases": serializer.data})


from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return


class WorkResultApiView(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    def post(self, request, format=None):
        lists_keys = list(request.data.keys())
        # print(lists_keys)
        print(request.data)
        filters = {}
        tradeunioncrime = request.data.get("tradeunioncrime_id")
        tradeunionright = request.data.get("tradeunionright_id")
        groupofrights = request.data.get("groupofrights_id")
        print(groupofrights)
        meetingsright = request.data.get("meetingsright_id")
        сonvention87 = request.data.get("сonvention87_id")
        tradeunionbuildingsright = request.data.get("tradeunionbuildingsright_id")
        createorganizationright = request.data.get("createorganizationright_id")

        createTradeUnionRight = request.data.get("createTradeUnionRight_id")
        electionsRight = request.data.get("electionsRight_id")
        сonversationRight = request.data.get("сonversationRight_id")
        tradeUnionActivityRight = request.data.get("tradeUnionActivityRight_id")
        createStrikeRight = request.data.get("createStrikeRight_id")
        сonvention98 = request.data.get("сonvention98_id")
        antiTradeUnionDiscrimination = request.data.get("antiTradeUnionDiscrimination_id")

        сonvention135 = request.data.get("сonvention135_id")
        consultationRight = request.data.get("consultationRight_id")
        principleOfNonDiscrimination = request.data.get("principleOfNonDiscrimination_id")
        discriminatiOnVariousGrounds = request.data.get("discriminatiOnVariousGrounds_id")
        discriminationInVariousAreas = request.data.get("discriminationInVariousAreas_id")
        publicPolicyDiscrimination = request.data.get("publicPolicyDiscrimination_id")
        childLabor = request.data.get("childLabor_id")

        сonvention138 = request.data.get("сonvention138_id")
        сonvention182 = request.data.get("сonvention182_id")
        prohibitionOfForcedLabor = request.data.get("prohibitionOfForcedLabor_id")
        useOfForcedLabor = request.data.get("useOfForcedLabor_id")
        governmentCoercion = request.data.get("governmentCoercion_id")
        violationsUsingCompulsoryLabor = request.data.get("violationsUsingCompulsoryLabor_id")
        failureSystemicMeasures = request.data.get("failureSystemicMeasures_id")
        intruder = request.data.get("intruder_id")

        natureviolation = request.data.get("natureviolation_id")
        rightsstate = request.data.get("rightsstate_id")
        victimsituation = request.data.get("victimsituation_id")
        tradeUnionSituation = request.data.get("tradeUnionSituation_id")
        work_tradeunionactivities = request.data.get("work_tradeunionactivities_id")
        user = request.data.get("user_id")
        victim = request.data.get("victim_id")
        source = request.data.get("source_id")
        print(source)
        country = request.data.get("country_id")
        region = request.data.get("region_id")





        if 'tradeunioncrime_id' in lists_keys:
            filters["tradeUnionCrime"] = tradeunioncrime
        if "tradeunionright_id" in lists_keys:
            filters["tradeUnionRight"] = tradeunionright
        if "groupofrights_id" in lists_keys:
            filters["groupOfRights"] = groupofrights
        if "meetingsright_id" in lists_keys:
            filters["meetingsRight"] = meetingsright
        if "сonvention87_id" in lists_keys:
            filters["сonvention87"] = сonvention87
        if "tradeunionbuildingsright_id" in lists_keys:
            filters["tradeUnionBuildingsRight"] = tradeunionbuildingsright
        if "createorganizationright_id" in lists_keys:
            filters["createOrganizationRight"] = createorganizationright

        if 'createTradeUnionRight_id' in lists_keys:
            filters["createTradeUnionRight"] = createTradeUnionRight
        if "electionsRight_id" in lists_keys:
            filters["electionsRight"] = electionsRight
        if "tradeUnionActivityRight_id" in lists_keys:
            filters["tradeUnionActivityRight"] = tradeUnionActivityRight
        if "createStrikeRight_id" in lists_keys:
            filters["createStrikeRight"] = createStrikeRight
        if "сonvention98_id" in lists_keys:
            filters["сonvention98"] = сonvention98
        if "antiTradeUnionDiscrimination_id" in lists_keys:
            filters["antiTradeUnionDiscrimination"] = antiTradeUnionDiscrimination
        if "сonversationRight_id" in lists_keys:
            filters["conversationRight"] = сonversationRight


        if 'сonvention135_id' in lists_keys:
            filters["сonvention135"] = сonvention135
        if "consultationRight_id" in lists_keys:
            filters["consultationRight"] = consultationRight
        if "principleOfNonDiscrimination_id" in lists_keys:
            filters["principleOfNonDiscrimination"] = principleOfNonDiscrimination
        if "discriminatiOnVariousGrounds_id" in lists_keys:
            filters["discriminatiOnVariousGrounds"] = discriminatiOnVariousGrounds
        if "discriminationInVariousAreas_id" in lists_keys:
            filters["discriminationInVariousAreas"] = discriminationInVariousAreas
        if "publicPolicyDiscrimination_id" in lists_keys:
            filters["publicPolicyDiscrimination"] = publicPolicyDiscrimination
        if "childLabor_id" in lists_keys:
            filters["childLabor"] = childLabor

        if 'сonvention138_id' in lists_keys:
            filters["сonvention138"] = сonvention138
        if "сonvention182_id" in lists_keys:
            filters["сonvention182"] = сonvention182
        if "prohibitionOfForcedLabor_id" in lists_keys:
            filters["prohibitionOfForcedLabor"] = prohibitionOfForcedLabor
        if "useOfForcedLabor_id" in lists_keys:
            filters["useOfForcedLabor"] = useOfForcedLabor
        if "governmentCoercion_id" in lists_keys:
            filters["governmentCoercion"] = governmentCoercion
        if "violationsUsingCompulsoryLabor_id" in lists_keys:
            filters["violationsUsingCompulsoryLabor"] = violationsUsingCompulsoryLabor
        if "failureSystemicMeasures_id" in lists_keys:
            filters["failureSystemicMeasures"] = failureSystemicMeasures
        if "intruder_id" in lists_keys:
            filters["intruder"] = intruder

        if 'natureviolation_id' in lists_keys:
            filters["violation_nature"] = natureviolation
        if "rightsstate_id" in lists_keys:
            filters["rights_state"] = rightsstate
        if "victimsituation_id" in lists_keys:
            filters["victim_situation"] = victimsituation
        if "tradeUnionSituation_id" in lists_keys:
            filters["tradeUnionSituation"] = tradeUnionSituation
        if "source_id" in lists_keys:
            filters["source"] = source
        if "country_id" in lists_keys:
            filters["country"] = country
        if "region_id" in lists_keys:
            filters["region"] = region
        if "work_tradeunionactivities_id" in lists_keys:
            filters["trade_union_activities"] = work_tradeunionactivities
        if "user_id" in lists_keys:
            filters["user"] = user
        if "victim_id" in lists_keys:
            filters["victim"] = victim

        print(filters)
        # cases = WorkCase.objects.all()
        workcases = WorkCase.objects.filter(**filters)
        serializer = WorkResultSerializer(workcases, many=True)
        return Response(serializer.data)


class StrikeResultApiView(APIView):
    def post(self, request):
        filters = request.data
        # cases = Card.objects.all()
        cards = Card.objects.filter(**filters)
        serializer = StrikeResultSerializer(cards, many=True)
        return Response(serializer.data)
