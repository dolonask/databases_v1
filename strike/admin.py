from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from .models import *
from import_export import resources, fields


class CardResource(resources.ModelResource):
    name = fields.Field(column_name=Card._meta.get_field('name').verbose_name, attribute='name')
    card_sources = fields.Field(column_name=Card._meta.get_field('card_sources').verbose_name, attribute='card_sources',
                                widget=ManyToManyWidget(Source, field='name'))
    source_url = fields.Field(column_name=Card._meta.get_field('source_url').verbose_name, attribute='source_url')
    source_content = fields.Field(column_name=Card._meta.get_field('source_content').verbose_name,
                                  attribute='source_content')
    country = fields.Field(column_name=Card._meta.get_field('country').verbose_name, attribute='country',
                           widget=ForeignKeyWidget(Country, field='name'))
    region = fields.Field(column_name=Card._meta.get_field('region').verbose_name, attribute='region',
                          widget=ForeignKeyWidget(Region, field='name'))
    city_name = fields.Field(column_name=Card._meta.get_field('city_name').verbose_name, attribute='city_name')
    company_name = fields.Field(column_name=Card._meta.get_field('company_name').verbose_name, attribute='company_name')
    company_ownership_type = fields.Field(column_name=Card._meta.get_field('company_ownership_type').verbose_name,
                                          attribute='company_ownership_type',
                                          widget=ForeignKeyWidget(OwnerShipType, field='name'))




    company_country_name = fields.Field(column_name=Card._meta.get_field('company_country_name').verbose_name,
                                        attribute='company_country_name')

    company_is_tnk_member = fields.Field(column_name=Card._meta.get_field('company_is_tnk_member').verbose_name,
                                         attribute='company_is_tnk_member')
    company_tnk_name = fields.Field(column_name=Card._meta.get_field('company_tnk_name').verbose_name,
                                    attribute='company_tnk_name')
    company_employees_count = fields.Field(column_name=Card._meta.get_field('company_employees_count').verbose_name,
                                           attribute='company_employees_count',
                                           widget=ForeignKeyWidget(EmployeesCount, field='choice'))


    count_strike_participants = fields.Field(column_name=Card._meta.get_field('count_strike_participants').verbose_name,
                                             attribute='count_strike_participants',
                                             widget=ForeignKeyWidget(ParticipantsCount, field='choice'))
    card_demand_categories = fields.Field(column_name=Card._meta.get_field('card_demand_categories').verbose_name,
                                          attribute='card_demand_categories',
                                          widget=ManyToManyWidget(DemandCategory, field='demand_cat_name'))
    economic_demands = fields.Field(column_name=Card._meta.get_field('economic_demands').verbose_name,
                                    attribute='economic_demands',
                                    widget=ManyToManyWidget(EconomicDemand, field='name'))
    economic_another = fields.Field(column_name=Card._meta.get_field('economic_another').verbose_name,
                                    attribute='economic_another')
    politic_demands = fields.Field(column_name=Card._meta.get_field('politic_demands').verbose_name,
                                   attribute='politic_demands',
                                   widget=ManyToManyWidget(PoliticDemand, field='name'))
    politic_another = fields.Field(column_name=Card._meta.get_field('politic_another').verbose_name,
                                   attribute='politic_another')
    combo_demands = fields.Field(column_name=Card._meta.get_field('combo_demands').verbose_name,
                                 attribute='combo_demands',
                                 widget=ManyToManyWidget(ComboDemand, field='name'))
    combo_another = fields.Field(column_name=Card._meta.get_field('combo_another').verbose_name,
                                 attribute='combo_another')
    start_date = fields.Field(column_name=Card._meta.get_field('start_date').verbose_name, attribute='start_date')
    end_date = fields.Field(column_name=Card._meta.get_field('end_date').verbose_name, attribute='end_date')
    tradeunionChoice = fields.Field(column_name=Card._meta.get_field('tradeunionChoice').verbose_name,
                                    attribute='tradeunionChoice',
                                    widget=ForeignKeyWidget(TradeunionChoice, field='name'))
    tradeunionChoiceAnother = fields.Field(column_name=Card._meta.get_field('tradeunionChoiceAnother').verbose_name,
                                           attribute='tradeunionChoiceAnother')
    date_create = fields.Field(column_name=Card._meta.get_field('date_create').verbose_name,
                               attribute='date_create')
    date_update = fields.Field(column_name=Card._meta.get_field('date_update').verbose_name,
                               attribute='date_update')
    active = fields.Field(column_name=Card._meta.get_field('active').verbose_name,
                          attribute='active')

    added_by = fields.Field(column_name=Card._meta.get_field('added_by').verbose_name,
                            attribute='added_by',
                            widget=ForeignKeyWidget(settings.AUTH_USER_MODEL, field='username'))
    initiator = fields.Field(column_name=Card._meta.get_field('initiator').verbose_name,
                             attribute='initiator',
                             widget=ForeignKeyWidget(Initiator, field='name'))
    tradeunion_data = fields.Field(column_name=Card._meta.get_field('tradeunion_data').verbose_name,
                                   attribute='tradeunion_data',
                                   widget=ForeignKeyWidget(TradeunionData, field='tradeUnion_name'))
    personGroupInfo = fields.Field(column_name=Card._meta.get_field('personGroupInfo').verbose_name,
                                           attribute='personGroupInfo',
                              widget=ForeignKeyWidget(PersonGroupInfo, field='groupCharacter__name'))
    employear = fields.Field(column_name=Card._meta.get_field('employear').verbose_name,
                             attribute='employear',
                             widget=ForeignKeyWidget(Employer, field='emp_name'))
    duration = fields.Field(column_name=Card._meta.get_field('duration').verbose_name,
                            attribute='duration',
                            widget=ForeignKeyWidget(StrikeCharacter, field='name'))
    meeting_requirements = fields.Field(column_name=Card._meta.get_field('meeting_requirements').verbose_name,
                                        attribute='meeting_requirements',
                                        widget=ForeignKeyWidget(MeetingRequirment, field='name'))
    story = fields.Field(column_name=Card._meta.get_field('story').verbose_name,
                         attribute='story')
    reasons_for_strike = fields.Field(column_name=Card._meta.get_field('reasons_for_strike').verbose_name,
                                      attribute='reasons_for_strike')
    change_number_participants = fields.Field(column_name=Card._meta.get_field('change_number_participants').verbose_name,
                                              attribute='change_number_participants')
    initiators_and_participants = fields.Field(column_name=Card._meta.get_field('initiators_and_participants').verbose_name,
                                               attribute='initiators_and_participants')
    state_position = fields.Field(column_name=Card._meta.get_field('state_position').verbose_name,
                                  attribute='state_position')
    results_so_far = fields.Field(column_name=Card._meta.get_field('results_so_far').verbose_name,
                                  attribute='results_so_far')
    additional_information = fields.Field(column_name=Card._meta.get_field('additional_information').verbose_name,
                                          attribute='additional_information')
    case_text = fields.Field(column_name=Card._meta.get_field('case_text').verbose_name,
                             attribute='case_text')

    class Meta:
        model = Card
        exclude = ('id',
                   'active',
                   'comment')


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CardResource


admin.site.register(Card, CaseAdmin)
admin.site.register(CardFile)
admin.site.register(CardPhoto)
