from django.contrib import admin
from .models import Source, Country, Region, OwnerShipType, EmployeesCount, ParticipantsCount, DemandCategory


admin.site.register(Source)
admin.site.register(Country)
admin.site.register(Region)
admin.site.register(OwnerShipType)
admin.site.register(EmployeesCount)
admin.site.register(ParticipantsCount)
admin.site.register(DemandCategory)
# Register your models here.
