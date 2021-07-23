from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'statistica/home.html', {})


def migrant_analytic(request):
    return render(request, 'statistica/migrant_search.html', {})


def strike_analytic(request):
    return render(request, 'statistica/strike_search.html', {})


def work_analytic(request):
    return render(request, 'statistica/work_search.html', {})