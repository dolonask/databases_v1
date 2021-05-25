from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from .models import Case, IndividualInfo, PersonGroup, Company, Entrepreneur, CasePhoto, CaseFile


class PhotoForm(forms.ModelForm):

    class Meta:
        model = CasePhoto
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple':'True'}),
        }

class FileForm(forms.ModelForm):

    class Meta:
        model = CaseFile
        fields = ['file']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'class': 'form-control', 'multiple':'True'}),
        }


class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = '__all__'
        exclude =['active', 'user','personGroupInfo','individualInfo', 'company', 'entrepreneur']

        widgets = {
            'case_name': forms.TextInput(attrs={'class': 'form-control'}),
            'victim_status': forms.Select(attrs={'class': 'form-control'}),
            'banOnEntry': forms.Select(attrs={'class': 'form-control', 'onchange': "onBanChanged(this.value);"}),
            'banOnEntryAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'source': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onSourceChanged(this.value);"}),
            'source_url': forms.URLInput(attrs={'class': 'form-control'}),
            'source_content': forms.Textarea(attrs={'class': 'form-control'}),
            'violated_right': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onRightChanged(this.value);"}),
            'violatedRightAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),
            'end_date': forms.DateInput(
                attrs={'class': 'form-control', 'value': datetime.now().strftime("%d-%m-%Y"), 'type': 'date'}),
            'victim': forms.Select(attrs={'class': 'form-control', 'onchange': "onVictimChanged(this.value);"}),
            'intruder': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onIntruderChanged(this.value);"}),
            'government_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'local_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'police_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'control_agency_name': forms.TextInput(attrs={'class': 'form-control'}),
            'case_additional': forms.Textarea(attrs={'class': 'form-control'}),
            'story': forms.Textarea(attrs={'class': 'form-control'}),
            'actions': forms.Textarea(attrs={'class': 'form-control'}),
            'final': forms.Textarea(attrs={'class': 'form-control'}),
            'violation_nature': forms.Select(attrs={'class': 'form-control'}),
            'rights_state': forms.Select(attrs={'class': 'form-control', 'onchange': "onRights_StateChanged(this.value);"}),
            'rights_state_another': forms.TextInput(attrs={'class': 'form-control'}),
            'victim_situation': forms.Select(attrs={'class': 'form-control', 'onchange': "onVictim_SituationChanged(this.value);"}),
            'victim_situation_another': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionSituation': forms.Select(attrs={'class': 'form-control', 'onchange': "onTradeUnionSituationChanged(this.value);"}),
            'tradeUnionSituation_another': forms.TextInput(attrs={'class': 'form-control'}),
            'tradeUnionCount': forms.Select(attrs={'class': 'form-control'}),
            'frequent_problems': forms.Textarea(attrs={'class': 'form-control'}),
            'decision': forms.Textarea(attrs={'class': 'form-control'}),
            'advice': forms.Textarea(attrs={'class': 'form-control'}),
            'has_violation_in_covid': forms.Select(attrs={'class': 'form-control'}),
            'violationType': forms.Select(attrs={'class': 'form-control', 'onchange': "onViolationTypeChanged(this.value);"}),
            'violationType_another': forms.TextInput(attrs={'class': 'form-control'}),
            'changesInSalary': forms.Select(attrs={'class': 'form-control', 'onchange': "onChangesInSalaryChanged(this.value);"}),
            'changesInSalary_another': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        source = cleaned_data.get("source")
        source_url = cleaned_data.get("source_url")
        source_content = cleaned_data.get("source_content")

        if source:
            for item in source:
                if item.id == 2 and (source_url is None or source_content is None):
                    self.add_error('source_url', "Укажите источник информации (ссылку)" )
                    self.add_error('source_content', "Если нет ссылки, то перенесите сюда текст статьи/сообщения ")



    def __init__(self, *args, **kwargs):
        super(CaseForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.error_messages = {'required': 'Необходимо ввести значение'}




class VictimForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }



class IndividualForm(forms.ModelForm):
    class Meta:
        model = IndividualInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'onchange': "onGenderChanged(this.value);"}),
            'gender_another': forms.TextInput(attrs={'class': 'form-control'}),
            'contacts': forms.TextInput(attrs={'class': 'form-control'}),
            'education': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.Select(attrs={'class': 'form-control', 'onchange': "onCountryChanged(this.value);"}),
            'countryAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'city_name': forms.TextInput(attrs={'class': 'form-control'}),
            'countryFrom': forms.Select(attrs={'class': 'form-control', 'onchange': "onCountryFromChanged(this.value);"}),
            'countryFromAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'city_name_from': forms.TextInput(attrs={'class': 'form-control'}),
            'wayOfArrival': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onWayArrivalChanged(this.value);"}),
            'wayOfArrivalAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'wayOfFindingWork': forms.Select(
                attrs={'class': 'form-control', 'onchange': "onWayFindingChanged(this.value);"}),
            'wayOfFindingWorkAnother': forms.TextInput(attrs={'class': 'form-control'}),
            'hasRegistration': forms.Select(attrs={'class': 'form-control'}),
            'tradeUnionMembership': forms.Select(attrs={'class': 'form-control'}),
            'experience': forms.TextInput(attrs={'class': 'form-control'}),
            'hasAgreement': forms.Select(attrs={'class': 'form-control', 'onchange': "onAgreementChanged(this.value);"}),
            'agreementDetailYes': forms.Select(attrs={'class': 'form-control'}),
            'agreementDetailNo': forms.Select(attrs={'class': 'form-control'}),
            'agreementLang': forms.TextInput(attrs={'class': 'form-control'}),
            'understoodTheContents': forms.Select(attrs={'class': 'form-control'}),
            'workBookStatus': forms.Select(attrs={'class': 'form-control'}),
            'workingDayDuration': forms.Select(attrs={'class': 'form-control'}),
            'hasOverResponsibilities': forms.Select(attrs={'class': 'form-control'}),
            'wayOfGettingSalary': forms.Select(attrs={'class': 'form-control'}),
        }



class GroupForm(forms.ModelForm):
    class Meta:
        model = PersonGroup
        fields = '__all__'

        widgets = {
            'amount': forms.TextInput(attrs={'class': 'form-control'}),
            'groupType': forms.Select(attrs={'class': 'form-control'}),
            'workDescription': forms.TextInput(attrs={'class': 'form-control'}),
            'membership': forms.Select(attrs={'class': 'form-control'}),
        }





class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'product_type': forms.TextInput(attrs={'class': 'form-control'}),
            'ownership': forms.Select(attrs={'class': 'form-control', 'onchange': "onOwnershipChanged(this.value);"}),
            'branch': forms.TextInput(attrs={'class': 'form-control'}),
            'company_experience': forms.TextInput(attrs={'class': 'form-control'}),
            'emp_count': forms.Select(attrs={'class': 'form-control'}),
            'additional': forms.Textarea(attrs={'class': 'form-control'}),
            'country_from': forms.TextInput(attrs={'class': 'form-control'}),
            'is_tnk_member': forms.Select(attrs={'class': 'form-control', 'onchange': "onTnkChanged(this.value);"}),
            'tnk_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def is_valid(self):
        pass

    def clean(self):
        cleaned_data = super().clean()
        print(cleaned_data)

class EntrepreneurForm(forms.ModelForm):
    class Meta:
        model = Entrepreneur
        fields = '__all__'
        widgets = {
            'entrepreneur_name': forms.TextInput(attrs={'class': 'form-control'}),
            'entrepreneur_age': forms.Select(attrs={'class': 'form-control'}),
            'entrepreneur_gender': forms.Select(attrs={'class': 'form-control'}),
            'entrepreneur_address': forms.TextInput(attrs={'class': 'form-control'}),
            'entrepreneur_workPurpose': forms.CheckboxSelectMultiple(
                attrs={'class': 'select'}),
            'entrepreneur_emp_count': forms.Select(attrs={'class': 'form-control'}),
            'entrepreneur_doAgreement': forms.Select(attrs={'class': 'form-control'}),
            'entrepreneur_payWay': forms.Select(attrs={'class': 'form-control'}),
            'entrepreneur_hireWay': forms.CheckboxSelectMultiple(
                attrs={'class': 'checkbox-list-none', 'onchange': "onHireWayChanged(this.value);"}),
            'entrepreneur_hireWayAnother': forms.TextInput(attrs={'class': 'form-control'}),
        }

