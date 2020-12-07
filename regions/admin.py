from django.contrib.gis.admin import OSMGeoAdmin
from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import County,  Headquarter, RegionalOffice, FieldOffice 

# Register your models here.
class CountyAdmin(OSMGeoAdmin):
    list_display = ('name', 'county')
admin.site.register(County, LeafletGeoAdmin)


class HeadquarterAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')

admin.site.register(Headquarter, LeafletGeoAdmin)
class RegionalOfficeAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'headquarter')

admin.site.register(RegionalOffice, LeafletGeoAdmin)

class FieldOfficeAdmin(OSMGeoAdmin):
    list_display = ('name', 'location', 'region')
admin.site.register(FieldOffice, LeafletGeoAdmin)

