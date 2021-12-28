import django_filters
from django import forms
from django_filters import DateFilter, CharFilter, ChoiceFilter, ModelChoiceFilter

from .models import *


def countries(request):
    return Country.objects.filter(active=True).all()



# def users(request):
#     return User.objects.filter().all()


class MigrantFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='Создан с',
                            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='Создан по',
                          widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    date_update = DateFilter(field_name="date_update", lookup_expr='gte', label='Обновлен с',
                            widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    end_update = DateFilter(field_name="date_update", lookup_expr='lte', label='Обновлен по',
                          widget=forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'date'}))
    # user = ModelChoiceFilter(queryset='user', label='Монитор', widget=forms.Select(attrs={'class': 'form-control'}))
    # case_name = CharFilter(field_name="case_name", lookup_expr='icontains', label='Название/описание карточки', widget=forms.TextInput(attrs={'class': 'form-control'})),
    case_name = CharFilter(field_name="case_name", lookup_expr='icontains',
                           label='Название/описание карточки',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    individualInfo_name = CharFilter(field_name="individualInfo__name", lookup_expr='icontains',
                                     label='Имя/название пострадавшего',
                                     widget=forms.TextInput(attrs={'class': 'form-control'}))
    country = ModelChoiceFilter(field_name='country', queryset=countries, label='Страна', widget=forms.Select(attrs={'class': 'form-control'}))
    region = ModelChoiceFilter(queryset=Region.objects.all(), field_name="region", label='Регион', widget=forms.Select(attrs={'class': 'form-control'}))
    # note = CharFilter(field_name='name', lookup_expr='icontains')

    # class Meta:
    #     model = Case
    #     fields = {
    #               'region',
    #               'country'
    #              }
    #     widgets ={
    #         'country':forms.Select(attrs={'class': 'form-control',}),
    #         'region':forms.Select(attrs={'class': 'form-control',})
    #     }
    # exclude = ['customer', 'date_created']
