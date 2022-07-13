from django.contrib import admin

from django.contrib import admin

# Importar las clases del modelo
from proyectoUno.models import Edificio, Departamento

# Edificio
class EdificioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'direccion', 'ciudad','tipo')
    search_fields = ('nombre', 'ciudad','tipo' )

admin.site.register(Edificio, EdificioAdmin)


class DepartamentoAdmin(admin.ModelAdmin):

    list_display = ('propietario', 'costo', 'numCuartos')
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)