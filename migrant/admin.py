
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Case, Employee, CasePhoto, CaseFile
from django.contrib.auth.models import Group, User

class CasePhotoInline(admin.StackedInline):
    model = CasePhoto
    extra = 1


class CaseFileInline(admin.StackedInline):
    model = CaseFile
    extra = 1


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    search_fields = ('case_name',)
    list_display = ('id', 'case_name', 'date_create', 'date_update')
    list_display_links = ('id', 'case_name')
    list_filter = ('date_create', 'date_update', 'company', 'country', 'region', 'victim_status', 'banOnEntry',
                   'banned_country', 'violated_right',
                    'case_date', 'start_date', 'end_date', 'victim',
                   'intruder', 'government_agency_name', 'local_agency_name', 'police_agency_name', 'control_agency_name',
                   'company', 'entrepreneur', 'violation_nature', 'rights_state',
                   'victim_situation', 'tradeUnionSituation',
                   'tradeUnionCount', 'case_additional_info', 'frequent_problems', 'decision', 'advice', 'has_violation_in_covid',
                   'violationType', 'changesInSalary', 'user')
    readonly_fields = ('get_photo', 'get_file')
    inlines = [CasePhotoInline, CaseFileInline]
    # show_full_result_count = True
    # list_editable = ('active',)

    def get_photo(self, obj):
        photos = CasePhoto.objects.filter(card_id=obj.id)
        if photos:
            html_photo = ''
            for photo in photos:
                html_photo += f'<img src="{photo.photo.url}" width=250><hr>\n'
            return mark_safe(html_photo)
        else:
            return '-'
    get_photo.short_description = 'Изображения'

    def get_file(self, obj):
        files = CaseFile.objects.filter(card_id=obj.id)
        if files:
            html_photo = ''
            for file in files:
                html_photo += f'<a href="#">{file.file.url}</a><hr>\n'
            return mark_safe(html_photo)
        else:
            return '-'
    get_photo.short_description = 'Файлы'


# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     search_fields = ('user', 'country')
#     list_display = ('id', 'user', 'country')
#     list_display_links = ('id', 'user')
#     list_filter = ('country',)


admin.site.unregister(Group)
admin.site.unregister(User)
