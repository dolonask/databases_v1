from datetime import datetime

from django import forms
from .models import Case, IndividualInfo, GroupOfPersons, TradeUnionInfo, Company, CaseFile, CasePhoto


class CaseFileForm(forms.ModelForm):
    class Meta:
        model = CaseFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': 'True'}),
        }


class CasePhotoForm(forms.ModelForm):
    class Meta:
        model = CasePhoto
        fields = ['photo']
        widgets = {
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple': 'True'}),
        }


class TradeUnionInfoForm(forms.ModelForm):
    class Meta:
        model = TradeUnionInfo
        fields = '__all__'
        widgets = {
            'tradeunion_name': forms.TextInput(attrs={'class': 'form-control'}),
            'branch_name': forms.TextInput(attrs={'class': 'form-control'}),
            'victim_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contacts': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CompanyInfoForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'ownership': forms.Select(attrs={'class': 'form-control', 'onchange': "onOwnershipChanged(this.value);"}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_count': forms.Select(attrs={'class': 'form-control'}),
            'additional': forms.Textarea(attrs={'class': 'form-control'}),
            'country_from': forms.TextInput(attrs={'class': 'form-control'}),
            'is_tnk_member': forms.Select(attrs={'class': 'form-control', 'onchange': "onTnkChanged(this.value);"}),
            'tnk_name': forms.TextInput(attrs={'class': 'form-control'}),
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
            'groupOfRights': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onGroupOfRightsChanged(this.value);"}),
            'tradeUnionRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeUnionRightChanged(this.value);"}),
            'tradeUnionRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionCrime': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeUnionCrimeChanged(this.value);"}),
            'tradeUnionCrimeAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'meetingsRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onMeetingsRightChanged(this.value);"}),
            'meetingsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionBuildingsRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeUnionBuildingsRightChanged(this.value);"}),
            'tradeUnionBuildingsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'createOrganizationRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onCreateOrganizationRightChanged(this.value);"}),
            'createOrganizationRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'createTradeUnionRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onCreateTradeUnionRightChanged(this.value);"}),
            'createTradeUnionRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'electionsRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onElectionsRightChanged(this.value);"}),
            'electionsRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionActivityRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeUnionActivityRightChanged(this.value);"}),
            'tradeUnionActivityRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'createStrikeRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onСreateStrikeRightChanged(this.value);"}),
            'createStrikeRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'antiTradeUnionDiscrimination': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onAntiTradeUnionDiscriminationChanged(this.value);"}),
            'antiTradeUnionDiscriminationAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'сonvention135': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onConvention135Changed(this.value);"}),
            'сonvention135Another': forms.TextInput(attrs={'class': 'form-control'}),
            'consultationRight': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onConsultationRightChanged(this.value);"}),
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
            'failureSystemicMeasures': forms.Select(attrs={'class': 'form-control'}),
            'victim': forms.Select(attrs={'class': 'form-control', 'onchange': "onVictimChanged(this.value);"}),
            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),

            'intruder': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onIntruderChanged(this.value);"}),
            'intruderAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'government_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'local_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'police_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'control_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'exact_data': forms.Textarea(attrs={'class': 'form-control'}),
            'case_description': forms.Textarea(attrs={'class': 'form-control'}),
            'actions': forms.Textarea(attrs={'class': 'form-control'}),
            'result': forms.Textarea(attrs={'class': 'form-control'}),
            'violation_nature': forms.Select(attrs={'class': 'form-control'}),
            'rights_state': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onRights_stateChanged(this.value);"}),
            'rights_state_another': forms.TextInput(attrs={'class': 'form-control'}),

            'victim_situation': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onVictim_situationChanged(this.value);"}),
            'victim_situation_another': forms.TextInput(attrs={'class': 'form-control'}),

            'tradeUnionSituation': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onTradeUnionSituationChanged(this.value);"}),
            'tradeUnionSituation_another': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionCount': forms.Select(attrs={'class': 'form-control'}),
            'case_text': forms.Textarea(attrs={'class': 'form-control'}),

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
        widgets = {
            'is_anonim': forms.Select(attrs={'class': 'form-control', 'onchange': "onIndAnonimChanged(this.value);"}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'member_of_tradeunion': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onIndTradeUnionMemberChanged(this.value);"}),
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
        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control', 'onchange': "onGroupTypeChanged(this.value);"}),
            'type_another': forms.TextInput(attrs={'class': 'form-control'}),
            'membership': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onGroupMembershipChanged(this.value);"}),
            'membership_another': forms.TextInput(attrs={'class': 'form-control'}),
        }
