
from django.contrib import admin
from .models import Case, Employee


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    search_fields = ('case_name',)
    list_display = ('id', 'case_name', 'date_create', 'date_update')
    list_display_links = ('id', 'case_name')
    list_filter = ('date_create', 'date_update')
    show_full_result_count = True
    # list_editable = ('active',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ('user', 'country')
    list_display = ('id', 'user', 'country')
    list_display_links = ('id', 'user')
    list_filter = ('country',)


# admin.site.register(CaseAdmin)
# admin.site.register(Employee)
