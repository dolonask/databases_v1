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

class WorkResultApiView(APIView):

    def post(self, request):
        filters = request.data
        # cases = WorkCase.objects.all()
        workcases = WorkCase.objects.filter(**filters)
        serializer = WorkResultSerializer(workcases, many=True)
        return Response({"workcases": serializer.data})


class StrikeResultApiView(APIView):

    def post(self, request):
        filters = request.data
        # cases = Card.objects.all()
        cards = Card.objects.filter(**filters)
        serializer = StrikeResultSerializer(cards, many=True)
        return Response(serializer.data)
