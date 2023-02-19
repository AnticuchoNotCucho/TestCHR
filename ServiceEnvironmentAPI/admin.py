from django.contrib import admin
from .models import Proyecto


class ProyectoAdmin(admin.ModelAdmin):
    list_display = (
        'numero', 'nombre', 'tipo', 'region', 'titular', 'tipologia', 'inversion', 'fecha', 'estado')


admin.site.register(Proyecto, ProyectoAdmin)
