from django.shortcuts import render, redirect

from .forms import CaseForm, CompanyForm, IndividualForm, VictimForm, GroupForm, EntrepreneurForm

# Create your views here.

def append_case(request):

    if request.method == 'POST':
        form = CaseForm(request.POST)
        companyForm = CompanyForm(request.POST)
        individualForm = IndividualForm(request.POST)
        victimForm = VictimForm(request.POST)
        groupForm = GroupForm(request.POST)
        entrepreneurForm = EntrepreneurForm(request.POST)

        if form.is_valid():

            cleaned_data = form.cleaned_data;

            if cleaned_data['company']:
                form_data = companyForm.cleaned_data;
                print(form_data)
            form = form.save(commit=False)
            form.user = request.user


            form.save()

            return redirect('migrant_case')

    else:
        form = CaseForm
        companyForm=CompanyForm
        individualForm =IndividualForm
        victimForm=VictimForm
        groupForm=GroupForm
        entrepreneurForm=EntrepreneurForm

    return render(request,
                  'migrant/append_case.html',
                  context={
                      'form': form,
                      'companyForm': companyForm,
                      'individualForm': individualForm,
                      'victimForm': victimForm,
                      'groupForm': groupForm,
                      'entrepreneurForm': entrepreneurForm,
                  })


def cases(request):
    pass
