from django.contrib import admin
from GameMap.models import Location


class LocationAdmin(admin.ModelAdmin):
    list_display = ('locationId',)


admin.site.register(Location, LocationAdmin)
