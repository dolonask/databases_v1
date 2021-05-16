from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import http
from django_tables2 import SingleTableView

from .tables import CardTable
from .forms import CardForm
from .models import Card

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin

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

class FilteredPersonListView(SingleTableMixin, FilterView):
    table_class = CardTable
    model = Card
    template_name = 'strike/strikes.html'

    filterset_class = FilterView

@login_required
def strikes(request):
    return render(request,'strike/strikes.html', {'cards':Card.objects.all()})