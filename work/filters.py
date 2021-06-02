import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, ModelChoiceFilter

from strike.models import Initiator
from .models import *

class WorkFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # note = CharFilter(field_name='name', lookup_expr='icontains')
    start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',
                            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',
                          widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    # case_name = CharFilter(field_name="case_name", lookup_expr='icontains', label='Название/описание карточки', widget=forms.TextInput(attrs={'class': 'form-control'})),
    name = CharFilter(field_name="name", lookup_expr='icontains',
                           label='Название/описание карточки',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    # individualInfo_name = CharFilter(field_name="individualInfo__name", lookup_expr='icontains',
    #                                  label='Имя/название пострадавшего',
    #                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = ModelChoiceFilter(field_name='country', queryset=Country.objects.filter(active = True).all(), label='Страна', widget=forms.Select(attrs={'class': 'form-control'}))
    region = ModelChoiceFilter(field_name="region", queryset=Region.objects.none(), label='Регион', widget=forms.Select(attrs={'class': 'form-control'}))
    initiator = ModelChoiceFilter(field_name="initiator", queryset=Initiator.objects.all(), label='Инициатор', widget=forms.Select(attrs={'class': 'form-control'}))


    # class Meta:
    #     model = Case
    #     fields = ['case_name', 'country', 'region', ]
    #     # exclude = ['customer', 'date_created']