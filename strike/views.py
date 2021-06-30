from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from io import BytesIO, StringIO
from django.template.loader import get_template
from xhtml2pdf import pisa

from .filters import CardFilter
from .forms import *
from .models import *


@login_required()
def add_case(request):
    general_tabs_fields = ['name',
                           'card_sources',
                           'source_url',
                           'source_content',
                           'country',
                           'region',
                           'city_name',
                           'company_name',
                           'company_ownership_type',
                           'company_is_tnk_member',
                           'company_tnk_name',
                           'company_employees_count',
                           'count_strike_participants',
                           'card_demand_categories',
                           'economic_demands',
                           'politic_demands',
                           'combo_demands',
                           'start_date',
                           'end_date',
                           'tradeunionChoice',
                           'tradeunionChoiceAnother',
                           'economic_another',
                           'politic_another',
                           'combo_another',
                           ]
    initiator_tab_fields = ['initiator']
    description_tab_fields = ['duration',
                              'meeting_requirements',
                              'story',
                              'reasons_for_strike',
                              'change_number_participants',
                              'initiators_and_participants',
                              'state_position',
                              'results_so_far',
                              'additional_information',

                              ]
    if request.method == "POST":
        form = CardForm(request.POST)
        tradeUnionForm = TradeunionForm(request.POST)
        personGroupInfoForm = PersonGroupInfoForm(request.POST)
        # individualForm = IndividualForm(request.POST)

        individualFormSet = IndividualFormSet(data=request.POST)


        employerForm = EmployerForm(request.POST)
        photoForm = CardPhotoForm(request.POST)
        fileForm = CardFileForm(request.POST)

        if form.is_valid():
            case = form.save(commit=False)

            if tradeUnionForm.is_valid():
                case.tradeunion_data = tradeUnionForm.save()
            if personGroupInfoForm.is_valid():
                case.personGroupInfo = personGroupInfoForm.save()
            # if individualFormSet.is_valid():
            #     for individualForm in individualFormSet.forms:
            #         ind = individualForm.save(commit = False)
            #         ind.card = case
            #         ind.save()

            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.card = case
               # individualFormSet.save()
            if employerForm.is_valid():
                case.employear = employerForm.save()


            case.added_by = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form.save_m2m()




            # if individualForm.is_valid():
            #     individualForm = individualForm.save(commit=False)
            #     individualForm.card = form
            #     individualForm.save()
            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CardPhoto(photo=f, card=form)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CardFile(file=f, card=form)
                    file.save()

            return redirect('strike_case')
    else:
        form = CardForm
        tradeUnionForm = TradeunionForm
        personGroupInfoForm = PersonGroupInfoForm
        individualFormSet = IndividualFormSet(queryset=Individual.objects.none())
        employerForm = EmployerForm
        photoForm = CardPhotoForm
        fileForm = CardFileForm

    return render(request,'strike/add_case.html', context={
        'form':form,
        'tradeUnionForm':tradeUnionForm,
        'personGroupInfoForm':personGroupInfoForm,
        'individualFormSet':individualFormSet,
        'employerForm':employerForm,
        'photoForm':photoForm,
        'fileForm':fileForm,
        'general_tabs_fields':general_tabs_fields,
        'initiator_tab_fields':initiator_tab_fields,
        'description_tab_fields':description_tab_fields,
    })


def load_regions(request):
    country_id = request.GET.get('country_id')
    regions = Region.objects.filter(country=country_id).all()
    return render(request,'strike/region_dropdown.html',{'regions':regions})

@login_required()
def cases(request):
    cards = Card.objects.all().filter(active=True)
    myFilter = CardFilter(request.GET,queryset=cards)
    cards = myFilter.qs
    context = {'cards':cards, 'myFilter':myFilter}
    return render(request, 'strike/strike.html', context)


@login_required()
def delete_case(request, pk):
    case = Card.objects.get(id=pk).delete()
    return redirect('strikes_list')

@login_required()
def update_case(request,pk):

    case = Card.objects.get(id=pk)


    general_tabs_fields = ['name',
                           'card_sources',
                           'source_url',
                           'source_content',
                           'country',
                           'region',
                           'city_name',
                           'company_name',
                           'company_ownership_type',
                           'company_is_tnk_member',
                           'company_tnk_name',
                           'company_employees_count',
                           'count_strike_participants',
                           'card_demand_categories',
                           'economic_demands',
                           'politic_demands',
                           'combo_demands',
                           'start_date',
                           'end_date',
                           'tradeunionChoice',
                           'tradeunionChoiceAnother',
                           'economic_another',
                           'politic_another',
                           'combo_another',
                           ]
    initiator_tab_fields = ['initiator']
    description_tab_fields = ['duration',
                              'meeting_requirements',
                              'story',
                              'reasons_for_strike',
                              'change_number_participants',
                              'initiators_and_participants',
                              'state_position',
                              'results_so_far',
                              'additional_information',

                              ]
    if request.method == "POST":
        form = CardForm(request.POST, instance=case)
        tradeUnionForm = TradeunionForm(request.POST)
        personGroupInfoForm = PersonGroupInfoForm(request.POST)
        # individualForm = IndividualForm(request.POST)

        individualFormSet = IndividualFormSet(data = request.POST)


        employerForm = EmployerForm(request.POST)
        photoForm = CardPhotoForm(request.POST)
        fileForm = CardFileForm(request.POST)

        if form.is_valid():
            form.save(commit=False)

            if tradeUnionForm.is_valid():
                case.tradeunion_data = tradeUnionForm.save()
            if personGroupInfoForm.is_valid():
                case.personGroupInfo = personGroupInfoForm.save()
            # if individualFormSet.is_valid():
            #     for individualForm in individualFormSet.forms:
            #         ind = individualForm.save(commit = False)
            #         ind.card = case
            #         ind.save()

            for individual in individualFormSet:
                if individual.is_valid():
                    ind = individual.save(commit=False)
                    ind.card = case
               # individualFormSet.save()
            if employerForm.is_valid():
                case.employear = employerForm.save()


            case.added_by = request.user
            case.active = True
            case.save()

            if individualFormSet.is_valid():
                individualFormSet.save()

            form.save_m2m()




            # if individualForm.is_valid():
            #     individualForm = individualForm.save(commit=False)
            #     individualForm.card = form
            #     individualForm.save()
            if photoForm.is_valid():
                for f in request.FILES.getlist('photo'):
                    photo = CardPhoto(photo=f, card=form)
                    photo.save()
            if fileForm.is_valid():
                for f in request.FILES.getlist('file'):
                    file = CardFile(file=f, card=form)
                    file.save()

            return redirect('strikes_list')
    else:
        form = CardForm(instance=case)

        tradeUnionForm = TradeunionForm
        if case.tradeunion_data is not None:
            tradeUnionForm = TradeunionForm(instance=TradeunionData.objects.get(pk = case.tradeunion_data_id))

        personGroupInfoForm = PersonGroupInfoForm
        if case.personGroupInfo is not None:
            personGroupInfoForm = PersonGroupInfoForm(instance=PersonGroupInfo.objects.get(pk=case.personGroupInfo_id))

        individualForm = IndividualForm
        # if Individual.objects.exists(card=case.pk):
        #     individualForm = IndividualForm(instance=Individual.objects.get(card=case.pk))

        employerForm = EmployerForm
        if case.employear is not None:
            employerForm = EmployerForm(instance=Employer.objects.get(pk=case.employear_id))

        photoForm = CardPhotoForm
        fileForm = CardFileForm

    return render(request, 'strike/add_case.html', context={
        'form': form,
        'tradeUnionForm': tradeUnionForm,
        'personGroupInfoForm': personGroupInfoForm,
        'individualForm': individualForm,
        'employerForm': employerForm,
        'photoForm': photoForm,
        'fileForm': fileForm,
        'general_tabs_fields': general_tabs_fields,
        'initiator_tab_fields': initiator_tab_fields,
        'description_tab_fields': description_tab_fields,
    })


def add_comment(request, pk):
    card = Card.objects.get(id=pk)
    if request.method == 'POST':
        data = request.POST
        data._mutable = True
        data['card'] = card.id
        form = CardCommentForm(data)
        if form.is_valid():
            form.save()
            return redirect('strikes_list')
    else:
        form = CardCommentForm()
    return render(request, 'strike/add_comment.html', {'form': form, 'card': card})


def show_comments(request, pk):
    comments = CardComment.objects.filter(card_id=pk, active=True)
    return render(request, 'strike/show_comments.html', {'comments': comments})


def delete_comment(request, pk):
    card_comment = CardComment.objects.get(id=pk).delete()
    card_comment.save()
    return redirect('strike_card_show_comments', card_comment.card_id)


def case_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    comments = CardComment.objects.filter(card_id=pk)
    template_path = 'strike/strike_pdf.html'
    context = {'card': card, 'comments': comments}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        BytesIO(html.encode('UTF-8')), dest=response, encoding='utf-8')
        # StringIO(html.encode("UTF-8")), response, encoding='UTF-8')
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def case_download_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    card = get_object_or_404(Card, pk=pk)
    template_path = 'strike/strike_pdf.html'
    context = {'card': card}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(
        BytesIO(html.encode('UTF-8')), dest=response, encoding='utf-8')
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response