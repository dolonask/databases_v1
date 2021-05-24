from datetime import datetime

from django import forms

from .models import Card, TradeunionData, Individual, Employer, CardFile, CardPhoto, Region


class RegionForm(forms.ModelForm):
    class Meta:
        model = Region
        fields= '__all__'



class CardFileForm(forms.ModelForm):
    class Meta:
        model = CardFile
        fields = ['file']

class CardPhotoForm(forms.ModelForm):
    class Meta:
        model = CardPhoto
        fields = ['file']


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'


class PersonGroupForm(forms.ModelForm):
    class Meta:
        model = TradeunionData
        fields = '__all__'


class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'
        exclude = ['card']


class TradeunionForm(forms.ModelForm):
    class Meta:
        model = TradeunionData
        fields = '__all__'


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        # fields = ['name', 'card_sources', 'source_url', 'source_content', 'country', 'region',
        #           'city_name', 'company_name', 'company_ownership_type','company_is_tnk_member','company_tnk_name','company_employees_count',
        #           'count_strike_participants','card_demand_categories', 'start_date', 'end_date', 'has_trade_union',
        #           ]

        fields = '__all__'
        exclude = ['added_by', 'is_active', 'tradeunion_data', 'employear']
        # region = forms.ModelChoiceField(queryset=Region.objects.all().filter(country=), to_field_name='region_name')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'card_sources': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onSourceChanged(this.value);"}),
            'source_url': forms.URLInput(attrs={'class': 'form-control'}),
            'source_content': forms.Textarea(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'city_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_ownership_type': forms.Select(attrs={'class': 'form-control'}),
            'company_is_tnk_member': forms.CheckboxInput(
                attrs={'class': 'form-check-label', 'id': 'company_is_tnk_member'}),
            'company_tnk_name': forms.TextInput(attrs={'class': 'form-control'}),

            'company_employees_count': forms.Select(attrs={'class': 'form-control'}),
            'count_strike_participants': forms.Select(attrs={'class': 'form-control'}),

            'card_demand_categories': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'id': 'card_demands'}),

            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),

            'has_trade_union': forms.Select(attrs={'class': 'form-control'}),
            'initiator': forms.Select(attrs={'class': 'form-control'}),
            'person_character': forms.Select(attrs={'class': 'form-control'}),
            # 'is_active': forms.CheckboxInput(attrs={'class': 'form-check-label'}),
            # 'trade_union': forms.TextInput(attrs={'class': 'form-control'}),
            # 'phone_number_union': forms.TextInput(attrs={'class': 'form-select'}),
            # 'address_union': forms.TextInput(attrs={'class': 'form-select'}),
            # 'group': forms.Select(attrs={'class': 'form-control'}),
            # 'union_membership': forms.Select(attrs={'class': 'form-control'}),
            # 'first_name': forms.TextInput(attrs={'class': 'form-select'}),
            # 'last_name': forms.TextInput(attrs={'class': 'form-select'}),
            # 'gender': forms.Select(attrs={'class': 'form-control'}),
            # 'age': forms.Select(attrs={'class': 'form-control'}),
            # 'profession': forms.TextInput(attrs={'class': 'form-select'}),
            # 'employer': forms.TextInput(attrs={'class': 'form-select'}),
            # 'phone_number_employer': forms.TextInput(attrs={'class': 'form-select'}),
            # 'address_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'meeting_requirements': forms.Select(attrs={'class': 'form-control'}),

        }
