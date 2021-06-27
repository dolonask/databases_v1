
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
    list_filter = ('date_create', 'date_update', 'company', 'country')
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
