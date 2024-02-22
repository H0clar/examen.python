from django.contrib import admin
from .models import Cliente  # Asegúrate de importar el modelo Cliente desde tu models.py






@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('rut', 'nombre', 'apellido', 'sector', 'estado', 'tipo_usuario')
    list_filter = ('sector', 'estado', 'tipo_usuario')
    search_fields = ('rut', 'nombre', 'apellido')
