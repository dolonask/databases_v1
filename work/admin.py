from django.contrib import admin

# Register your models here.
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from django.contrib.auth.models import User

from .models import *


class CaseResource(resources.ModelResource):
    case_name = fields.Field(column_name=Case._meta.get_field('case_name').verbose_name, attribute='case_name')
    source = fields.Field(column_name=Case._meta.get_field('source').verbose_name, attribute='source', widget=ManyToManyWidget(Source, field='name'))
    source_another = fields.Field(column_name='Другое (Источник)', attribute='source_another')
    source_url = fields.Field(column_name=Case._meta.get_field('source_url').verbose_name, attribute='source_url')
    source_content = fields.Field(column_name=Case._meta.get_field('source_content').verbose_name, attribute='source_content')
    country = fields.Field(column_name=Case._meta.get_field('country').verbose_name, attribute='country',
                           widget=ForeignKeyWidget(Country, field='name'))
    region = fields.Field(column_name=Case._meta.get_field('region').verbose_name, attribute='region',
                          widget=ForeignKeyWidget(Region, field='name'))
    date_create = fields.Field(column_name=Case._meta.get_field('date_create').verbose_name, attribute='date_create')
    date_update = fields.Field(column_name=Case._meta.get_field('date_update').verbose_name, attribute='date_update')
    city_name = fields.Field(column_name=Case._meta.get_field('city_name').verbose_name, attribute='city_name')
    case_company_name = fields.Field(column_name=Case._meta.get_field('case_company_name').verbose_name,
                                     attribute='case_company_name')
    groupOfRights = fields.Field(column_name=Case._meta.get_field('groupOfRights').verbose_name,
                                 attribute='groupOfRights', widget=ForeignKeyWidget(GroupOfRights, field='name'))
    tradeUnionRight = fields.Field(column_name=Case._meta.get_field('tradeUnionRight').verbose_name,
                                   attribute='tradeUnionRight', widget=ForeignKeyWidget(TradeUnionRight, field='name'))
    tradeUnionRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionRightAnother').verbose_name,
                                          attribute='tradeUnionRightAnother')
    tradeUnionCrime = fields.Field(column_name=Case._meta.get_field('tradeUnionCrime').verbose_name,
                                   attribute='tradeUnionCrime', widget=ForeignKeyWidget(TradeUnionCrime, field='name'))
    tradeUnionCrimeAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionCrimeAnother').verbose_name,
                                          attribute='tradeUnionCrimeAnother')
    meetingsRight = fields.Field(column_name=Case._meta.get_field('meetingsRight').verbose_name,
                                 attribute='meetingsRight', widget=ForeignKeyWidget(MeetingsRight, field='name'))
    meetingsRightAnother = fields.Field(column_name=Case._meta.get_field('meetingsRightAnother').verbose_name,
                                        attribute='meetingsRightAnother')
    сonvention87 = fields.Field(column_name=Case._meta.get_field('сonvention87').verbose_name,
                                attribute='сonvention87', widget=ForeignKeyWidget(Сonvention87, field='name'))
    tradeUnionBuildingsRight = fields.Field(column_name=Case._meta.get_field('tradeUnionBuildingsRight').verbose_name,
                                            attribute='tradeUnionBuildingsRight', widget=ForeignKeyWidget(TradeUnionBuildingsRight, field='name'))
    tradeUnionBuildingsRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionBuildingsRightAnother').verbose_name,
                                                   attribute='tradeUnionBuildingsRightAnother')
    createOrganizationRight = fields.Field(column_name=Case._meta.get_field('createOrganizationRight').verbose_name,
                                           attribute='createOrganizationRight',
                                           widget=ForeignKeyWidget(CreateOrganizationRight, field='name'))
    createOrganizationRightAnother = fields.Field(column_name=Case._meta.get_field('createOrganizationRightAnother').verbose_name,
                                                  attribute='createOrganizationRightAnother')
    createTradeUnionRight = fields.Field(column_name=Case._meta.get_field('createTradeUnionRight').verbose_name,
                                         attribute='createTradeUnionRight',
                                         widget=ForeignKeyWidget(CreateTradeUnionRight, field='name'))
    createTradeUnionRightAnother = fields.Field(column_name=Case._meta.get_field('createTradeUnionRightAnother').verbose_name,
                                                attribute='createTradeUnionRightAnother')
    electionsRight = fields.Field(column_name=Case._meta.get_field('electionsRight').verbose_name,
                                  attribute='electionsRight', widget=ForeignKeyWidget(ElectionsRight, field='name'))
    electionsRightAnother = fields.Field(column_name=Case._meta.get_field('electionsRightAnother').verbose_name,
                                         attribute='electionsRightAnother')
    tradeUnionActivityRight = fields.Field(column_name=Case._meta.get_field('tradeUnionActivityRight').verbose_name,
                                           attribute='tradeUnionActivityRight',
                                           widget=ForeignKeyWidget(TradeUnionActivityRight, field='name'))
    tradeUnionActivityRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionActivityRightAnother').verbose_name,
                                                  attribute='tradeUnionActivityRightAnother')
    createStrikeRight = fields.Field(column_name=Case._meta.get_field('createStrikeRight').verbose_name,
                                     attribute='createStrikeRight', widget=ForeignKeyWidget(CreateStrikeRight, field='name'))
    createStrikeRightAnother = fields.Field(column_name=Case._meta.get_field('createStrikeRightAnother').verbose_name,
                                            attribute='createStrikeRightAnother')
    сonvention98 = fields.Field(column_name=Case._meta.get_field('сonvention98').verbose_name,
                                attribute='сonvention98', widget=ForeignKeyWidget(Сonvention98, field='name'))
    antiTradeUnionDiscrimination = fields.Field(column_name=Case._meta.get_field('antiTradeUnionDiscrimination').verbose_name,
                                                attribute='antiTradeUnionDiscrimination',
                                                widget=ForeignKeyWidget(AntiTradeUnionDiscrimination, field='name'))
    antiTradeUnionDiscriminationAnother = fields.Field(column_name=Case._meta.get_field('antiTradeUnionDiscriminationAnother').verbose_name,
                                                       attribute='antiTradeUnionDiscriminationAnother')
    conversationRight = fields.Field(column_name=Case._meta.get_field('conversationRight').verbose_name,
                                     attribute='conversationRight', widget=ForeignKeyWidget(СonversationRight, field='name'))
    conversationRightAnother = fields.Field(column_name=Case._meta.get_field('conversationRightAnother').verbose_name,
                                            attribute='conversationRightAnother')
    сonvention135 = fields.Field(column_name=Case._meta.get_field('сonvention135').verbose_name, attribute='сonvention135',
                                 widget=ForeignKeyWidget(Сonvention135, field='name'))
    сonvention135Another = fields.Field(column_name=Case._meta.get_field('сonvention135Another').verbose_name,
                                        attribute='сonvention135Another')
    consultationRight = fields.Field(column_name=Case._meta.get_field('consultationRight').verbose_name,
                                     attribute='consultationRight', widget=ForeignKeyWidget(ConsultationRight, field='name'))
    consultationRightAnother = fields.Field(column_name=Case._meta.get_field('consultationRightAnother').verbose_name,
                                            attribute='consultationRightAnother')
    principleOfNonDiscrimination = fields.Field(column_name=Case._meta.get_field('principleOfNonDiscrimination').verbose_name,
                                                attribute='principleOfNonDiscrimination',
                                                widget=ForeignKeyWidget(PrincipleOfNonDiscrimination, field='name'))
    discriminatiOnVariousGrounds = fields.Field(column_name=Case._meta.get_field('discriminatiOnVariousGrounds').verbose_name,
                                                attribute='discriminatiOnVariousGrounds',
                                                widget=ForeignKeyWidget(DiscriminatiOnVariousGrounds, field='name'))
    discriminationInVariousAreas = fields.Field(column_name=Case._meta.get_field('discriminationInVariousAreas').verbose_name,
                                                attribute='discriminationInVariousAreas',
                                                widget=ForeignKeyWidget(DiscriminationInVariousAreas, field='name'))
    discriminationInVariousAreasAnother = fields.Field(column_name=Case._meta.get_field('discriminationInVariousAreasAnother').verbose_name,
                                                       attribute='discriminationInVariousAreasAnother')
    publicPolicyDiscrimination = fields.Field(column_name=Case._meta.get_field('publicPolicyDiscrimination').verbose_name,
                                              attribute='publicPolicyDiscrimination',
                                              widget=ForeignKeyWidget(PublicPolicyDiscrimination, field='name'))
    childLabor = fields.Field(column_name=Case._meta.get_field('childLabor').verbose_name, attribute='childLabor',
                              widget=ForeignKeyWidget(ChildLabor, field='name'))
    сonvention138 = fields.Field(column_name=Case._meta.get_field('сonvention138').verbose_name, attribute='сonvention138',
                                 widget=ForeignKeyWidget(Сonvention138, field='name'))
    convention182 = fields.Field(column_name=Case._meta.get_field('convention182').verbose_name, attribute='convention182',
                                 widget=ForeignKeyWidget(Сonvention182, field='name'))
    prohibitionOfForcedLabor = fields.Field(column_name=Case._meta.get_field('prohibitionOfForcedLabor').verbose_name,
                                            attribute='prohibitionOfForcedLabor',
                                            widget=ForeignKeyWidget(ProhibitionOfForcedLabor, field='name'))
    useOfForcedLabor = fields.Field(column_name=Case._meta.get_field('useOfForcedLabor').verbose_name,
                                    attribute='useOfForcedLabor',
                                    widget=ForeignKeyWidget(UseOfForcedLabor, field='name'))
    governmentCoercion = fields.Field(column_name=Case._meta.get_field('governmentCoercion').verbose_name,
                                      attribute='governmentCoercion',
                                      widget=ForeignKeyWidget(GovernmentCoercion, field='name'))
    violationsUsingCompulsoryLabor = fields.Field(column_name=Case._meta.get_field('violationsUsingCompulsoryLabor').verbose_name,
                                                  attribute='violationsUsingCompulsoryLabor',
                                                  widget=ForeignKeyWidget(ViolationsUsingCompulsoryLabor, field='name'))
    failureSystemicMeasures = fields.Field(column_name=Case._meta.get_field('failureSystemicMeasures').verbose_name,
                                           attribute='failureSystemicMeasures',
                                           widget=ForeignKeyWidget(FailureSystemicMeasures, field='name'))
    start_date = fields.Field(column_name=Case._meta.get_field('start_date').verbose_name, attribute='start_date')
    end_date = fields.Field(column_name=Case._meta.get_field('end_date').verbose_name, attribute='end_date')
    victim = fields.Field(column_name=Case._meta.get_field('victim').verbose_name, attribute='victim',
                          widget=ForeignKeyWidget(Victim, field='name'))
    tradeUnionInfo = fields.Field(column_name=Case._meta.get_field('tradeUnionInfo').verbose_name, attribute='tradeUnionInfo',
                                  widget=ForeignKeyWidget(TradeUnionInfo, field='tradeunion_name'))
    groupOfPersons = fields.Field(column_name=Case._meta.get_field('groupOfPersons').verbose_name, attribute='groupOfPersons',
                                  widget=ForeignKeyWidget(GroupOfRights, field='name'))
    intruder = fields.Field(column_name=Case._meta.get_field('intruder').verbose_name, attribute='intruder',
                            widget=ManyToManyWidget(Intruder, field='name'))
    intruderAnother = fields.Field(column_name=Case._meta.get_field('intruderAnother').verbose_name, attribute='intruderAnother')
    government_agency_name = fields.Field(column_name=Case._meta.get_field('government_agency_name').verbose_name,
                                          attribute='government_agency_name')
    local_agency_name = fields.Field(column_name=Case._meta.get_field('local_agency_name').verbose_name,
                                     attribute='local_agency_name')
    police_agency_name = fields.Field(column_name=Case._meta.get_field('police_agency_name').verbose_name,
                                      attribute='police_agency_name')
    company = fields.Field(column_name=Case._meta.get_field('company').verbose_name, attribute='company',
                           widget=ForeignKeyWidget(Company, field='company_name'))
    exact_data = fields.Field(column_name=Case._meta.get_field('exact_data').verbose_name, attribute='exact_data')
    case_description = fields.Field(column_name=Case._meta.get_field('case_description').verbose_name, attribute='case_description')
    tradeunion_actions = fields.Field(column_name=Case._meta.get_field('tradeunion_actions').verbose_name, attribute='tradeunion_actions')
    case_result = fields.Field(column_name=Case._meta.get_field('case_result').verbose_name, attribute='case_result')
    violation_nature = fields.Field(column_name=Case._meta.get_field('violation_nature').verbose_name, attribute='violation_nature',
                                    widget=ForeignKeyWidget(NatureViolation, field='name'))
    rights_state = fields.Field(column_name=Case._meta.get_field('rights_state').verbose_name, attribute='rights_state',
                                widget=ForeignKeyWidget(RightsState, field='name'))
    rights_state_another = fields.Field(column_name=Case._meta.get_field('rights_state_another').verbose_name,
                                        attribute='rights_state_another')
    victim_situation = fields.Field(column_name=Case._meta.get_field('victim_situation').verbose_name, attribute='victim_situation',
                                    widget=ForeignKeyWidget(VictimSituation, field='name'))
    victim_situation_another = fields.Field(column_name=Case._meta.get_field('victim_situation_another').verbose_name,
                                            attribute='victim_situation_another')
    tradeUnionSituation = fields.Field(column_name=Case._meta.get_field('tradeUnionSituation').verbose_name,
                                       attribute='tradeUnionSituation',
                                       widget=ForeignKeyWidget(TradeUnionSituation, field='name'))
    tradeUnionSituation_another = fields.Field(column_name=Case._meta.get_field('tradeUnionSituation_another').verbose_name,
                                               attribute='tradeUnionSituation_another')
    tradeUnionCount = fields.Field(column_name=Case._meta.get_field('tradeUnionCount').verbose_name,
                                   attribute='tradeUnionCount', widget=ForeignKeyWidget(TradeUnionCount, field='choice'))
    case_text = fields.Field(column_name=Case._meta.get_field('case_text').verbose_name, attribute='case_text')
    trade_union_activities = fields.Field(column_name=Case._meta.get_field('trade_union_activities').verbose_name,
                                          attribute='trade_union_activities', widget=ForeignKeyWidget(TradeUnionActivities, field='name'))
    trade_union_activities_another = fields.Field(column_name=Case._meta.get_field('trade_union_activities_another').verbose_name,
                                                  attribute='trade_union_activities_another')
    user = fields.Field(column_name=Case._meta.get_field('user').verbose_name, attribute='user',
                        widget=ForeignKeyWidget(User, field='username'))

    class Meta:
        model = Case
        exclude = ('id',
                   'active',
                   'comment')


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CaseResource
    list_display = ('case_name', 'user', 'date_create', 'date_update')

admin.site.register(Case, CaseAdmin)
