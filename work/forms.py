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

