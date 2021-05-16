from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import http
from django_tables2 import SingleTableView

from .tables import CardTable
from .forms import CardForm
from .models import Card

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .filters import CardFilter

@login_required
def append_case(request):

    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            # card = Cards.objects.create(**form.cleaned_data)
            # print(request.POST)
            form.user = request.user
            print(form.user)
            card = form.save()


            #return redirect('strike_case')
    else:
        form = CardForm()

    return render(request, 'strike/strike_case.html', {'form': form})
# Create your views here.

class StrikeListView(SingleTableView):
    model = Card
    table_class = CardTable
    template_name = 'strike/strikes.html'

def strikes_cases(request):
    cards = Card.objects.all()


class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = CardTable
    model = Card
    template_name = "strike/strikes.html"

    filterset_class = CardFilter

@login_required
def strikes(request):
    cards = Card.objects.all()
    return render(request,'strike/strike.html', {'cards':Card.objects.all()})


def cases(request):

    cards = Card.objects.all()

    myFilter = CardFilter(request.GET,queryset=cards)
    cards = myFilter.qs

    context = {'cards':cards, 'myFilter':myFilter}

    return render(request, 'strike/strike.html', context)


