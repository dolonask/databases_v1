from datetime import datetime

from django import forms
from django.forms import modelformset_factory

from .models import Card, TradeunionData, Individual, Employer, CardFile, CardPhoto, Region, PersonGroupInfo, CardComment


class CardFileForm(forms.ModelForm):
    class Meta:
        model = CardFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple':'True'}),
        }


class CardPhotoForm(forms.ModelForm):
    class Meta:
        model = CardPhoto
        fields = ['photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple':'True'}),
        }


class EmployerForm(forms.ModelForm):
    class Meta:
        model = Employer
        fields = '__all__'
        widgets = {
            'emp_name': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_contacts': forms.TextInput(attrs={'class': 'form-control'}),
        }


IndividualFormSet = modelformset_factory(
    Individual,
    fields=('__all__'),
    exclude = ['card', 'id'],
    widgets={
        'is_anonim':forms.Select(attrs={'class': 'form-control', 'onchange': "onIndividualAnonimChanged(this.value);"}),
        'individual_name':forms.TextInput(attrs={'class': 'form-control'}),
        'gender':forms.Select(attrs={'class': 'form-control'}),
        'age':forms.Select(attrs={'class': 'form-control'}),
        'profession':forms.TextInput(attrs={'class': 'form-control'}),
    },
    extra=1,
    absolute_max=10,
    max_num= 10
)

class IndividualForm(forms.ModelForm):
    class Meta:
        model = Individual
        fields = '__all__'
        exclude = ['card']
        widgets={
            'is_anonim':forms.Select(attrs={'class': 'form-control', 'onchange': "onIndividualAnonimChanged(this.value);"}),
            'individual_name':forms.TextInput(attrs={'class': 'form-control'}),
            'gender':forms.Select(attrs={'class': 'form-control'}),
            'age':forms.Select(attrs={'class': 'form-control'}),
            'profession':forms.TextInput(attrs={'class': 'form-control'}),
        }


class TradeunionForm(forms.ModelForm):
    class Meta:
        model = TradeunionData
        fields = '__all__'
        widgets = {
            'tradeUnion_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnion_contacts': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PersonGroupInfoForm(forms.ModelForm):
    class Meta:
        model = PersonGroupInfo
        fields = '__all__'
        widgets = {
            'groupCharacter': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onGroupCharacterChanged(this.value);"}),
            'groupCharacter_another': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionMembership': forms.Select(attrs={'class': 'form-control'}),
        }


class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        # fields = ['name', 'card_sources', 'source_url', 'source_content', 'country', 'region',
        #           'city_name', 'company_name', 'company_ownership_type','company_is_tnk_member','company_tnk_name','company_employees_count',
        #           'count_strike_participants','card_demand_categories', 'start_date', 'end_date', 'has_trade_union',
        #           ]

        fields = '__all__'
        exclude = ['added_by', 'is_active', 'tradeunion_data', 'employear', 'comment']
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
            'company_ownership_type': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onCompanyOwnershipChanged(this.value);"}),
            'company_is_tnk_member': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTnkChanged(this.value);"}),
            'company_tnk_name': forms.TextInput(attrs={'class': 'form-control'}),

            'company_employees_count': forms.Select(attrs={'class': 'form-control'}),
            'count_strike_participants': forms.Select(attrs={'class': 'form-control'}),

            'card_demand_categories': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'id': 'card_demands',
                       'onchange': "onCardDemandCategoriesChanged(this.value);"}),
            'economic_demands': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none','onchange': "onEconomicDemandsChanged(this.value);"}),
            'economic_another': forms.TextInput(attrs={'class': 'form-control'}),
            'politic_demands': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onPoliticDemandsChanged(this.value);"}),
            'politic_another': forms.TextInput(attrs={'class': 'form-control'}),
            'combo_demands': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onComboDemandsChanged(this.value);"}),
            'combo_another': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(format='%Y-%m-%d',
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%Y-%m-%d"), 'type': 'date'}),
            'end_date': forms.DateInput(format='%Y-%m-%d',
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%Y-%m-%d"), 'type': 'date'}),
            'date_type': forms.Select(
                attrs={'class': 'form-control', 'onchange': 'checkIntrud(this)', 'type': 'radio'}
            ),
            'tradeunionChoice': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeunionChoiceChanged(this.value);"}),
            'tradeunionChoiceAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'initiator': forms.Select(attrs={'class': 'form-control', 'onchange': "onInitiatorSelected(this.value);"}),
            'person_character': forms.Select(attrs={'class': 'form-control'}),
            'trade_union': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_number_union': forms.TextInput(attrs={'class': 'form-select'}),
            'address_union': forms.TextInput(attrs={'class': 'form-select'}),
            'group': forms.Select(attrs={'class': 'form-control'}),
            'union_membership': forms.Select(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-select'}),
            'last_name': forms.TextInput(attrs={'class': 'form-select'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'class': 'form-select'}),
            'employer': forms.TextInput(attrs={'class': 'form-select'}),
            'phone_number_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'address_employer': forms.TextInput(attrs={'class': 'form-select'}),
            'duration': forms.Select(attrs={'class': 'form-control'}),
            'meeting_requirements': forms.Select(attrs={'class': 'form-control'}),
            'story': forms.Textarea(attrs={'class': 'form-control'}),
            'reasons_for_strike': forms.Textarea(attrs={'class': 'form-control'}),
            'change_number_participants': forms.Textarea(attrs={'class': 'form-control'}),
            'initiators_and_participants': forms.Textarea(attrs={'class': 'form-control'}),
            'state_position': forms.Textarea(attrs={'class': 'form-control'}),
            'results_so_far': forms.Textarea(attrs={'class': 'form-control'}),
            'additional_information': forms.Textarea(attrs={'class': 'form-control'}),
            'case_text': forms.Textarea(attrs={'class': 'form-control'}),

        }

        def __init__(self, *args, **kwargs):

            super().__init__(*args, **kwargs)
            self.fields['region'].queryset = Region.objects.none()

            # if 'country' in self.data:
            #     try:
            #         country_id = int(self.data.get('country'))
            #         self.fields['region'].queryset = Region.objects.filter(country_id=country_id).order_by('name')
            #     except (ValueError, TypeError):
            #         pass  # invalid input from the client; ignore and fallback to empty City queryset
            # elif self.instance.pk:
            #     self.fields['region'].queryset = self.instance.country.region_set.order_by('name')


class CardCommentForm(forms.ModelForm):
    class Meta:
        model = CardComment
        fields = ['comment', 'card']
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }