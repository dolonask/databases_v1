import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, ModelChoiceFilter

from .models import *


class CardFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # note = CharFilter(field_name='name', lookup_expr='icontains')

    start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',
                            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',
                          widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_update = DateFilter(field_name="date_update", lookup_expr='gte', label='Обновлен с',
                            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_update = DateFilter(field_name="date_update", lookup_expr='lte', label='Обновлен по',
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
    #     model = Card
    #     fields = ['name', 'country', 'region', 'initiator',]
    #     widgets = {
    #         'name': forms.TextInput(attrs={'class': 'form-control'}),
    #         'country': forms.Select(attrs={'class': 'form-control'}),
    #         'region': forms.Select(attrs={'class': 'form-control'}),
    #         'initiator': forms.Select(attrs={'class': 'form-control'}),
    #         'start_date': forms.DateInput(attrs={'class': 'form-control'}),
    #         'end_date': forms.DateInput(attrs={'class': 'form-control'}),
    #     }
        # exclude = ['customer', 'date_created']