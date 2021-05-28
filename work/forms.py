from django import forms
from .models import Case, IndividualInfo, GroupOfPersons


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onSourceChanged(this.value);"}),
            'source_url': forms.URLInput(attrs={'class': 'form-control'}),
            'source_content': forms.Textarea(attrs={'class': 'form-control'}),
            'region': forms.Select(attrs={'class': 'form-control'}),
            'city_name': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'groupOfRights': forms.Select(attrs={'class': 'form-control', 'onchange': "onGroupOfRightsChanged(this.value);"}),
            'tradeUnionRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onTradeUnionRightChanged(this.value);"}),
            'tradeUnionRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionCrime': forms.Select(attrs={'class': 'form-control', 'onchange': "onTradeUnionCrimeChanged(this.value);"}),
            'tradeUnionCrimeAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'meetingsRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onMeetingsRightChanged(this.value);"}),
            'meetingsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionBuildingsRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onTradeUnionBuildingsRightChanged(this.value);"}),
            'tradeUnionBuildingsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'createOrganizationRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onCreateOrganizationRightChanged(this.value);"}),
            'createOrganizationRightAnother': forms.TextInput(attrs={'class': 'form-control'}),

        }

class VictimForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'

class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'


class GroupForm(forms.ModelForm):
    class Meta:
        model = GroupOfPersons
        fields = '__all__'

