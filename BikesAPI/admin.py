from django.contrib import admin
from .models import Station, Extra, Network, Location


class StationAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'free_bikes', 'empty_slots')


admin.site.register(Station, StationAdmin)
admin.site.register(Extra)
admin.site.register(Network)
admin.site.register(Location)

