from django.http import Http404
from django.shortcuts import render


# Create your views here.
def home(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        return render(request, 'statistica/home.html', {})
    else:
        raise Http404('Недостаточно прав!')


def migrant_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        return render(request, 'statistica/migrant_search.html', {})
    else:
        raise Http404('Недостаточно прав!')


def strike_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        return render(request, 'statistica/strike_search.html', {})
    else:
        raise Http404('Недостаточно прав!')


def work_analytic(request):
    if request.user.position.role_id == 1 or request.user.position.role_id == 2:
        return render(request, 'statistica/work_search.html', {})
    else:
        raise Http404('Недостаточно прав!')