from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse
from django.shortcuts import render


# Create your views here.
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