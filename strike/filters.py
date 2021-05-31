import django_filters
from django import forms
from django_filters import DateFilter

from .models import *


class CardFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date_create", lookup_expr='gte')
    start_date = DateFilter(field_name="date_create", lookup_expr='gte', label='с',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    end_date = DateFilter(field_name="date_create", lookup_expr='lte', label='по',  widget=forms.DateTimeInput(attrs={'type':'date'}))
    # note = CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Card
        fields = ['name', 'country', 'region', 'initiator']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'initiator': forms.Select(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'class': 'form-control'}),
        }
        # exclude = ['customer', 'date_created']