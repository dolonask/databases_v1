import django_filters
from django import forms
from django_filters import DateFilter, CharFilter

from .models import *

class MigrantFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # note = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Case
        fields = ['case_name', 'country', 'region', ]
        # exclude = ['customer', 'date_created']