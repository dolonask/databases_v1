from django import forms
from .models import Case, IndividualInfo, GroupOfPersons, TradeUnionInfo


class TradeUnionInfoForm(forms.ModelForm):
    class Meta:
        model = TradeUnionInfo
        fields = '__all__'
        widgets={
            'tradeunion_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

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
            'createTradeUnionRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onCreateTradeUnionRightChanged(this.value);"}),
            'createTradeUnionRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'electionsRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onElectionsRightChanged(this.value);"}),
            'electionsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionActivityRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onTradeUnionActivityRightChanged(this.value);"}),
            'tradeUnionActivityRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'createStrikeRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onСreateStrikeRightChanged(this.value);"}),
            'createStrikeRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'antiTradeUnionDiscrimination': forms.Select(attrs={'class': 'form-control', 'onchange': "onAntiTradeUnionDiscriminationChanged(this.value);"}),
            'antiTradeUnionDiscriminationAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'сonvention135': forms.Select(attrs={'class': 'form-control', 'onchange': "onConvention135Changed(this.value);"}),
            'сonvention135Another': forms.TextInput(attrs={'class': 'form-control'}),
            'consultationRight': forms.Select(attrs={'class': 'form-control', 'onchange': "onConsultationRightChanged(this.value);"}),
            'consultationRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'discriminatiOnVariousGrounds': forms.Select(attrs={'class': 'form-control'}),
            'publicPolicyDiscrimination': forms.Select(attrs={'class': 'form-control'}),
            'childLabor': forms.Select(attrs={'class': 'form-control'}),
            'сonvention138': forms.Select(attrs={'class': 'form-control'}),
            'convention182': forms.Select(attrs={'class': 'form-control'}),
            'prohibitionOfForcedLabor': forms.Select(attrs={'class': 'form-control'}),
            'useOfForcedLabor': forms.Select(attrs={'class': 'form-control'}),
            'governmentCoercion': forms.Select(attrs={'class': 'form-control'}),
            'violationsUsingCompulsoryLabor': forms.Select(attrs={'class': 'form-control'}),
            'failureSystemicMeasures': forms.Select(attrs={'class': 'form-control'}),
            'victim': forms.Select(attrs={'class': 'form-control'}),


        }


class VictimForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'

class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'
        exclude = ['case']
        widgets={
            'is_anonim': forms.Select(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'member_of_tradeunion': forms.Select(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.Select(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'marital_status': forms.Select(attrs={'class': 'form-control'}),
            'position': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'is_official': forms.Select(attrs={'class': 'form-control'}),
            'has_agreement': forms.Select(attrs={'class': 'form-control'}),
            'agreementDetail': forms.Select(attrs={'class': 'form-control'}),
        }




class PersonGroupForm(forms.ModelForm):
    class Meta:
        model = GroupOfPersons
        fields = '__all__'
        widgets={
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'type_another': forms.TextInput(attrs={'class': 'form-control'}),
            'membership': forms.Select(attrs={'class': 'form-control'}),
            'membership_another': forms.TextInput(attrs={'class': 'form-control'}),
        }
