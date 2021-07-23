from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'statistica/home.html', {})


def migrant_analityc(request):
    return render(request, 'statistica/migrant_search.html', {})
