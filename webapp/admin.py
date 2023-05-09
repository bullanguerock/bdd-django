from django.contrib import admin
from webapp.models import Cliente
from webapp.models import Proveedor
from webapp.models import Producto_Servicio
from webapp.models import Solicitud
from webapp.models import Tecnico
from webapp.models import Protocolo_Mant

# Register your models here.

# Define the admin class
class ClienteAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Cliente._meta.fields]
# Register the admin class with the associated model
admin.site.register(Cliente, ClienteAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Proveedor._meta.fields]
# Register the admin class with the associated model
admin.site.register(Proveedor, ProveedorAdmin)

class Producto_ServicioAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Producto_Servicio._meta.fields]
# Register the admin class with the associated model
admin.site.register(Producto_Servicio, Producto_ServicioAdmin)

class SolicitudAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Solicitud._meta.fields]
# Register the admin class with the associated model
admin.site.register(Solicitud, SolicitudAdmin)

class TecnicoAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Tecnico._meta.fields]
# Register the admin class with the associated model
admin.site.register(Tecnico, TecnicoAdmin)

class Protocolo_MantAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Protocolo_Mant._meta.fields]
# Register the admin class with the associated model
admin.site.register(Protocolo_Mant, Protocolo_MantAdmin)

