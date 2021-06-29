
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Case, Employee, CasePhoto


class CasePhotoInline(admin.StackedInline):
    model = CasePhoto
    extra = 1


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    search_fields = ('case_name',)
    list_display = ('id', 'case_name', 'date_create', 'date_update')
    list_display_links = ('id', 'case_name')
    list_filter = ('date_create', 'date_update', 'company', 'country', 'region', 'victim_status', 'banOnEntry',
                   'banned_country', 'banOnEntryAnother', 'source', 'source_url', 'source_content', 'violated_right',
                   'violatedRightAnother', 'case_date', 'start_date', 'end_date', 'victim', 'individualInfo', 'personGroupInfo',
                   'intruder', 'government_agency_name', 'local_agency_name', 'police_agency_name', 'control_agency_name',
                   'company', 'entrepreneur', 'case_additional', 'story', 'actions', 'final', 'violation_nature', 'rights_state',
                   'rights_state_another', 'victim_situation', 'victim_situation_another', 'tradeUnionSituation', 'tradeUnionSituation_another',
                   'tradeUnionCount', 'case_additional_info', 'frequent_problems', 'decision', 'advice', 'has_violation_in_covid',
                   'violationType', 'violationType_another', 'changesInSalary', 'changesInSalary_another', 'user')
    readonly_fields = ('get_photo', )
    inlines = [CasePhotoInline]
    # show_full_result_count = True
    # list_editable = ('active',)

    def get_photo(self, obj):
        photos = CasePhoto.objects.filter(card_id=obj.id)
        if photos:
            html_photo = ''
            # print(photos)
            for photo in photos:
                html_photo += f'<img src="{photo.photo.url}" width=250><hr>\n'
            return mark_safe(html_photo)
        else:
            return '-'
    get_photo.short_description = 'Изображения'



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('user', 'country')
    list_display = ('id', 'user', 'country')
    list_display_links = ('id', 'user')
    list_filter = ('country',)


    # list_display = ('id', 'card_id', 'card_case_name')
    # fields = ('photo', 'card')
    # list_filter = ('card',)
    # search_fields = ('card.name', )
# admin.site.register(Case)
# admin.site.register(CasePhoto)
