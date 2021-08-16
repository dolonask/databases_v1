
from django.contrib import admin
from django.contrib.auth.models import Group, User
from import_export.admin import ImportExportModelAdmin
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from .models import *


class CaseResource(resources.ModelResource):
    case_name = fields.Field(column_name=Case._meta.get_field('case_name').verbose_name, attribute='case_name')

    country = fields.Field(column_name=Case._meta.get_field('country').verbose_name, attribute='country',
                           widget=ForeignKeyWidget(Country, field='name'))
    region = fields.Field(column_name=Case._meta.get_field('region').verbose_name, attribute='region',
                          widget=ForeignKeyWidget(Region, field='name'))
    victim_status = fields.Field(column_name=Case._meta.get_field('victim_status').verbose_name, attribute='victim_status',
                                 widget=ForeignKeyWidget(VictimStatus, field='name'))
    date_create = fields.Field(column_name=Case._meta.get_field('date_create').verbose_name, attribute='date_create')
    date_update = fields.Field(column_name=Case._meta.get_field('date_update').verbose_name, attribute='date_update')

    banOnEntry = fields.Field(column_name=Case._meta.get_field('banOnEntry').verbose_name, attribute='banOnEntry',
                              widget=ForeignKeyWidget(BanOnEntry, field='name'))

    # case_company_name = fields.Field(column_name=Case._meta.get_field('case_company_name').verbose_name,
    #                                  attribute='case_company_name')
    # groupOfRights = fields.Field(column_name=Case._meta.get_field('groupOfRights').verbose_name,
    #                              attribute='groupOfRights', widget=ForeignKeyWidget(GroupOfRights, field='name'))
    # tradeUnionRight = fields.Field(column_name=Case._meta.get_field('tradeUnionRight').verbose_name,
    #                                attribute='tradeUnionRight', widget=ForeignKeyWidget(TradeUnionRight, field='name'))
    # tradeUnionRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionRightAnother').verbose_name,
    #                                       attribute='tradeUnionRightAnother')
    # tradeUnionCrime = fields.Field(column_name=Case._meta.get_field('tradeUnionCrime').verbose_name,
    #                                attribute='tradeUnionCrime', widget=ForeignKeyWidget(TradeUnionCrime, field='name'))
    # tradeUnionCrimeAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionCrimeAnother').verbose_name,
    #                                       attribute='tradeUnionCrimeAnother')
    # meetingsRight = fields.Field(column_name=Case._meta.get_field('meetingsRight').verbose_name,
    #                              attribute='meetingsRight', widget=ForeignKeyWidget(MeetingsRight, field='name'))
    # meetingsRightAnother = fields.Field(column_name=Case._meta.get_field('meetingsRightAnother').verbose_name,
    #                                     attribute='meetingsRightAnother')
    # сonvention87 = fields.Field(column_name=Case._meta.get_field('сonvention87').verbose_name,
    #                             attribute='сonvention87', widget=ForeignKeyWidget(Сonvention87, field='name'))
    # tradeUnionBuildingsRight = fields.Field(column_name=Case._meta.get_field('tradeUnionBuildingsRight').verbose_name,
    #                                         attribute='tradeUnionBuildingsRight', widget=ForeignKeyWidget(TradeUnionBuildingsRight, field='name'))
    # tradeUnionBuildingsRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionBuildingsRightAnother').verbose_name,
    #                                                attribute='tradeUnionBuildingsRightAnother')
    # createOrganizationRight = fields.Field(column_name=Case._meta.get_field('createOrganizationRight').verbose_name,
    #                                        attribute='createOrganizationRight',
    #                                        widget=ForeignKeyWidget(CreateOrganizationRight, field='name'))
    # createOrganizationRightAnother = fields.Field(column_name=Case._meta.get_field('createOrganizationRightAnother').verbose_name,
    #                                               attribute='createOrganizationRightAnother')
    # createTradeUnionRight = fields.Field(column_name=Case._meta.get_field('createTradeUnionRight').verbose_name,
    #                                      attribute='createTradeUnionRight',
    #                                      widget=ForeignKeyWidget(CreateTradeUnionRight, field='name'))
    # createTradeUnionRightAnother = fields.Field(column_name=Case._meta.get_field('createTradeUnionRightAnother').verbose_name,
    #                                             attribute='createTradeUnionRightAnother')
    # electionsRight = fields.Field(column_name=Case._meta.get_field('electionsRight').verbose_name,
    #                               attribute='electionsRight', widget=ForeignKeyWidget(ElectionsRight, field='name'))
    # electionsRightAnother = fields.Field(column_name=Case._meta.get_field('electionsRightAnother').verbose_name,
    #                                      attribute='electionsRightAnother')
    # tradeUnionActivityRight = fields.Field(column_name=Case._meta.get_field('tradeUnionActivityRight').verbose_name,
    #                                        attribute='tradeUnionActivityRight',
    #                                        widget=ForeignKeyWidget(TradeUnionActivityRight, field='name'))
    # tradeUnionActivityRightAnother = fields.Field(column_name=Case._meta.get_field('tradeUnionActivityRightAnother').verbose_name,
    #                                               attribute='tradeUnionActivityRightAnother')
    # createStrikeRight = fields.Field(column_name=Case._meta.get_field('createStrikeRight').verbose_name,
    #                                  attribute='createStrikeRight', widget=ForeignKeyWidget(CreateStrikeRight, field='name'))
    # createStrikeRightAnother = fields.Field(column_name=Case._meta.get_field('createStrikeRightAnother').verbose_name,
    #                                         attribute='createStrikeRightAnother')
    # сonvention98 = fields.Field(column_name=Case._meta.get_field('сonvention98').verbose_name,
    #                             attribute='сonvention98', widget=ForeignKeyWidget(Сonvention98, field='name'))
    # antiTradeUnionDiscrimination = fields.Field(column_name=Case._meta.get_field('antiTradeUnionDiscrimination').verbose_name,
    #                                             attribute='antiTradeUnionDiscrimination',
    #                                             widget=ForeignKeyWidget(AntiTradeUnionDiscrimination, field='name'))
    # antiTradeUnionDiscriminationAnother = fields.Field(column_name=Case._meta.get_field('antiTradeUnionDiscriminationAnother').verbose_name,
    #                                                    attribute='antiTradeUnionDiscriminationAnother')
    # conversationRight = fields.Field(column_name=Case._meta.get_field('conversationRight').verbose_name,
    #                                  attribute='conversationRight', widget=ForeignKeyWidget(СonversationRight, field='name'))
    # conversationRightAnother = fields.Field(column_name=Case._meta.get_field('conversationRightAnother').verbose_name,
    #                                         attribute='conversationRightAnother')
    # сonvention135 = fields.Field(column_name=Case._meta.get_field('сonvention135').verbose_name, attribute='сonvention135',
    #                              widget=ForeignKeyWidget(Сonvention135, field='name'))
    # сonvention135Another = fields.Field(column_name=Case._meta.get_field('сonvention135Another').verbose_name,
    #                                     attribute='сonvention135Another')
    # consultationRight = fields.Field(column_name=Case._meta.get_field('consultationRight').verbose_name,
    #                                  attribute='consultationRight', widget=ForeignKeyWidget(ConsultationRight, field='name'))
    # consultationRightAnother = fields.Field(column_name=Case._meta.get_field('consultationRightAnother').verbose_name,
    #                                         attribute='consultationRightAnother')
    # principleOfNonDiscrimination = fields.Field(column_name=Case._meta.get_field('principleOfNonDiscrimination').verbose_name,
    #                                             attribute='principleOfNonDiscrimination',
    #                                             widget=ForeignKeyWidget(PrincipleOfNonDiscrimination, field='name'))
    # discriminatiOnVariousGrounds = fields.Field(column_name=Case._meta.get_field('discriminatiOnVariousGrounds').verbose_name,
    #                                             attribute='discriminatiOnVariousGrounds',
    #                                             widget=ForeignKeyWidget(DiscriminatiOnVariousGrounds, field='name'))
    # discriminationInVariousAreas = fields.Field(column_name=Case._meta.get_field('discriminationInVariousAreas').verbose_name,
    #                                             attribute='discriminationInVariousAreas',
    #                                             widget=ForeignKeyWidget(DiscriminationInVariousAreas, field='name'))
    # discriminationInVariousAreasAnother = fields.Field(column_name=Case._meta.get_field('discriminationInVariousAreasAnother').verbose_name,
    #                                                    attribute='discriminationInVariousAreasAnother')
    # publicPolicyDiscrimination = fields.Field(column_name=Case._meta.get_field('publicPolicyDiscrimination').verbose_name,
    #                                           attribute='publicPolicyDiscrimination',
    #                                           widget=ForeignKeyWidget(PublicPolicyDiscrimination, field='name'))
    # childLabor = fields.Field(column_name=Case._meta.get_field('childLabor').verbose_name, attribute='childLabor',
    #                           widget=ForeignKeyWidget(ChildLabor, field='name'))
    # сonvention138 = fields.Field(column_name=Case._meta.get_field('сonvention138').verbose_name, attribute='сonvention138',
    #                              widget=ForeignKeyWidget(Сonvention138, field='name'))
    # convention182 = fields.Field(column_name=Case._meta.get_field('convention182').verbose_name, attribute='convention182',
    #                              widget=ForeignKeyWidget(Сonvention182, field='name'))
    # prohibitionOfForcedLabor = fields.Field(column_name=Case._meta.get_field('prohibitionOfForcedLabor').verbose_name,
    #                                         attribute='prohibitionOfForcedLabor',
    #                                         widget=ForeignKeyWidget(ProhibitionOfForcedLabor, field='name'))
    # useOfForcedLabor = fields.Field(column_name=Case._meta.get_field('useOfForcedLabor').verbose_name,
    #                                 attribute='useOfForcedLabor',
    #                                 widget=ForeignKeyWidget(UseOfForcedLabor, field='name'))
    # governmentCoercion = fields.Field(column_name=Case._meta.get_field('governmentCoercion').verbose_name,
    #                                   attribute='governmentCoercion',
    #                                   widget=ForeignKeyWidget(GovernmentCoercion, field='name'))
    # violationsUsingCompulsoryLabor = fields.Field(column_name=Case._meta.get_field('violationsUsingCompulsoryLabor').verbose_name,
    #                                               attribute='violationsUsingCompulsoryLabor',
    #                                               widget=ForeignKeyWidget(ViolationsUsingCompulsoryLabor, field='name'))
    # failureSystemicMeasures = fields.Field(column_name=Case._meta.get_field('failureSystemicMeasures').verbose_name,
    #                                        attribute='failureSystemicMeasures',
    #                                        widget=ForeignKeyWidget(FailureSystemicMeasures, field='name'))
    # start_date = fields.Field(column_name=Case._meta.get_field('start_date').verbose_name, attribute='start_date')
    # end_date = fields.Field(column_name=Case._meta.get_field('end_date').verbose_name, attribute='end_date')
    # victim = fields.Field(column_name=Case._meta.get_field('victim').verbose_name, attribute='victim',
    #                       widget=ForeignKeyWidget(Victim, field='name'))
    # tradeUnionInfo = fields.Field(column_name=Case._meta.get_field('tradeUnionInfo').verbose_name, attribute='tradeUnionInfo',
    #                               widget=ForeignKeyWidget(TradeUnionInfo, field='tradeunion_name'))
    # groupOfPersons = fields.Field(column_name=Case._meta.get_field('groupOfPersons').verbose_name, attribute='groupOfPersons',
    #                               widget=ForeignKeyWidget(GroupOfRights, field='name'))
    # intruder = fields.Field(column_name=Case._meta.get_field('intruder').verbose_name, attribute='intruder',
    #                         widget=ManyToManyWidget(Intruder, field='name'))
    # intruderAnother = fields.Field(column_name=Case._meta.get_field('intruderAnother').verbose_name, attribute='intruderAnother')
    # government_agency_name = fields.Field(column_name=Case._meta.get_field('government_agency_name').verbose_name,
    #                                       attribute='government_agency_name')
    # local_agency_name = fields.Field(column_name=Case._meta.get_field('local_agency_name').verbose_name,
    #                                  attribute='local_agency_name')
    # police_agency_name = fields.Field(column_name=Case._meta.get_field('police_agency_name').verbose_name,
    #                                   attribute='police_agency_name')
    # company = fields.Field(column_name=Case._meta.get_field('company').verbose_name, attribute='company',
    #                        widget=ForeignKeyWidget(Company, field='company_name'))
    # exact_data = fields.Field(column_name=Case._meta.get_field('exact_data').verbose_name, attribute='exact_data')
    # case_description = fields.Field(column_name=Case._meta.get_field('case_description').verbose_name, attribute='case_description')
    # tradeunion_actions = fields.Field(column_name=Case._meta.get_field('tradeunion_actions').verbose_name, attribute='tradeunion_actions')
    # case_result = fields.Field(column_name=Case._meta.get_field('case_result').verbose_name, attribute='case_result')
    # violation_nature = fields.Field(column_name=Case._meta.get_field('violation_nature').verbose_name, attribute='violation_nature',
    #                                 widget=ForeignKeyWidget(NatureViolation, field='name'))
    # rights_state = fields.Field(column_name=Case._meta.get_field('rights_state').verbose_name, attribute='rights_state',
    #                             widget=ForeignKeyWidget(RightsState, field='name'))
    # rights_state_another = fields.Field(column_name=Case._meta.get_field('rights_state_another').verbose_name,
    #                                     attribute='rights_state_another')
    # victim_situation = fields.Field(column_name=Case._meta.get_field('victim_situation').verbose_name, attribute='victim_situation',
    #                                 widget=ForeignKeyWidget(VictimSituation, field='name'))
    # victim_situation_another = fields.Field(column_name=Case._meta.get_field('victim_situation_another').verbose_name,
    #                                         attribute='victim_situation_another')
    # tradeUnionSituation = fields.Field(column_name=Case._meta.get_field('tradeUnionSituation').verbose_name,
    #                                    attribute='tradeUnionSituation',
    #                                    widget=ForeignKeyWidget(TradeUnionSituation, field='name'))
    # tradeUnionSituation_another = fields.Field(column_name=Case._meta.get_field('tradeUnionSituation_another').verbose_name,
    #                                            attribute='tradeUnionSituation_another')
    # tradeUnionCount = fields.Field(column_name=Case._meta.get_field('tradeUnionCount').verbose_name,
    #                                attribute='tradeUnionCount', widget=ForeignKeyWidget(TradeUnionCount, field='choice'))
    # case_text = fields.Field(column_name=Case._meta.get_field('case_text').verbose_name, attribute='case_text')
    # trade_union_activities = fields.Field(column_name=Case._meta.get_field('trade_union_activities').verbose_name,
    #                                       attribute='trade_union_activities', widget=ForeignKeyWidget(TradeUnionActivities, field='name'))
    # trade_union_activities_another = fields.Field(column_name=Case._meta.get_field('trade_union_activities_another').verbose_name,
    #                                               attribute='trade_union_activities_another')
    # user = fields.Field(column_name=Case._meta.get_field('user').verbose_name, attribute='user')
    # comment = fields.Field(column_name=Case._meta.get_field('comment').verbose_name, attribute='comment',
    #                        widget=ForeignKeyWidget(CaseComment, 'comment'))

    class Meta:
        model = Case
        # fields = ('case_name', 'source', 'country')
        exclude = ('id',
                   'active',
                   'comment')


class CaseAdmin(ImportExportModelAdmin):
    resource_class = CaseResource


admin.site.register(Case, CaseAdmin)



admin.site.unregister(Group)
admin.site.unregister(User)

from django.conf import settings
from django.contrib import admin, messages
from django.contrib.admin.options import IS_POPUP_VAR
from django.contrib.admin.utils import unquote
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import (
    AdminPasswordChangeForm, UserChangeForm, UserCreationForm,
)
from django.contrib.auth.models import Group, User
from django.core.exceptions import PermissionDenied
from django.db import router, transaction
from django.http import Http404, HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import path, reverse
from django.utils.decorators import method_decorator
from django.utils.html import escape
from django.utils.translation import gettext, gettext_lazy as _
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from main import models

csrf_protect_m = method_decorator(csrf_protect)
sensitive_post_parameters_m = method_decorator(sensitive_post_parameters())


class MainCountryInline(admin.StackedInline):
    model = models.Country


class MainPositionInline(admin.StackedInline):
    model = models.Position


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    add_form_template = 'admin/auth/user/add_form.html'
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)
    inlines = [MainCountryInline, MainPositionInline]


    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets
        return super().get_fieldsets(request, obj)

    def get_form(self, request, obj=None, **kwargs):
        """
        Use special form during user creation
        """
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def get_urls(self):
        return [
                   path(
                       '<id>/password/',
                       self.admin_site.admin_view(self.user_change_password),
                       name='auth_user_password_change',
                   ),
               ] + super().get_urls()

    def lookup_allowed(self, lookup, value):
        # Don't allow lookups involving passwords.
        return not lookup.startswith('password') and super().lookup_allowed(lookup, value)

    @sensitive_post_parameters_m
    @csrf_protect_m
    def add_view(self, request, form_url='', extra_context=None):
        with transaction.atomic(using=router.db_for_write(self.model)):
            return self._add_view(request, form_url, extra_context)

    def _add_view(self, request, form_url='', extra_context=None):
        # It's an error for a user to have add permission but NOT change
        # permission for users. If we allowed such users to add users, they
        # could create superusers, which would mean they would essentially have
        # the permission to change users. To avoid the problem entirely, we
        # disallow users from adding users if they don't have change
        # permission.
        if not self.has_change_permission(request):
            if self.has_add_permission(request) and settings.DEBUG:
                # Raise Http404 in debug mode so that the user gets a helpful
                # error message.
                raise Http404(
                    'Your user does not have the "Change user" permission. In '
                    'order to add users, Django requires that your user '
                    'account have both the "Add user" and "Change user" '
                    'permissions set.')
            raise PermissionDenied
        if extra_context is None:
            extra_context = {}
        username_field = self.model._meta.get_field(self.model.USERNAME_FIELD)
        defaults = {
            'auto_populated_fields': (),
            'username_help_text': username_field.help_text,
        }
        extra_context.update(defaults)
        return super().add_view(request, form_url, extra_context)

    @sensitive_post_parameters_m
    def user_change_password(self, request, id, form_url=''):
        user = self.get_object(request, unquote(id))
        if not self.has_change_permission(request, user):
            raise PermissionDenied
        if user is None:
            raise Http404(_('%(name)s object with primary key %(key)r does not exist.') % {
                'name': self.model._meta.verbose_name,
                'key': escape(id),
            })
        if request.method == 'POST':
            form = self.change_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                change_message = self.construct_change_message(request, form, None)
                self.log_change(request, user, change_message)
                msg = gettext('Password changed successfully.')
                messages.success(request, msg)
                update_session_auth_hash(request, form.user)
                return HttpResponseRedirect(
                    reverse(
                        '%s:%s_%s_change' % (
                            self.admin_site.name,
                            user._meta.app_label,
                            user._meta.model_name,
                        ),
                        args=(user.pk,),
                        )
                )
        else:
            form = self.change_password_form(user)

        fieldsets = [(None, {'fields': list(form.base_fields)})]
        adminForm = admin.helpers.AdminForm(form, fieldsets, {})

        context = {
            'title': _('Change password: %s') % escape(user.get_username()),
            'adminForm': adminForm,
            'form_url': form_url,
            'form': form,
            'is_popup': (IS_POPUP_VAR in request.POST or
                         IS_POPUP_VAR in request.GET),
            'add': True,
            'change': False,
            'has_delete_permission': False,
            'has_change_permission': True,
            'has_absolute_url': False,
            'opts': self.model._meta,
            'original': user,
            'save_as': False,
            'show_save': True,
            **self.admin_site.each_context(request),
        }

        request.current_app = self.admin_site.name

        return TemplateResponse(
            request,
            self.change_user_password_template or
            'admin/auth/user/change_password.html',
            context,
            )

    def response_add(self, request, obj, post_url_continue=None):
        """
        Determine the HttpResponse for the add_view stage. It mostly defers to
        its superclass implementation but is customized because the User model
        has a slightly different workflow.
        """
        # We should allow further modification of the user just added i.e. the
        # 'Save' button should behave like the 'Save and continue editing'
        # button except in two scenarios:
        # * The user has pressed the 'Save and add another' button
        # * We are adding a user in a popup
        if '_addanother' not in request.POST and IS_POPUP_VAR not in request.POST:
            request.POST = request.POST.copy()
            request.POST['_continue'] = 1
        return super().response_add(request, obj, post_url_continue)
