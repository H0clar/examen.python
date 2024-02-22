from django.contrib import admin
from django.urls import path

from AguasNS.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio_view, name="inicio"),
    path('añadir_clientes/', añadir_clientes_view, name="añadir_clientes"),
    path('modificar_clientes/', modificar_clientes_view, name="modificar_clientes"),
    path('ver_clientes_activos/', ver_clientes_activos_view, name="ver_clientes_activos"),
    path('ver_clientes_inactivos/', ver_clientes_inactivos_view, name="ver_clientes_inactivos"),

    path('insertar_cliente/', insertar_cliente, name="insertar_cliente"),
    path('mostrar_todos_clientes_activos/', mostrar_todos_clientes_activos, name="mostrar_todos_clientes_activos"),
    path('mostrar_todos_clientes_inactivos/', mostrar_todos_clientes_inactivos, name="mostrar_todos_clientes_inactivos"),

    path('buscar_cliente_por_rut/', buscar_cliente_por_rut, name='buscar_cliente_por_rut'),

    # Agregamos la nueva ruta para actualizar datos del cliente
    path('actualizar_datos_cliente/', actualizar_datos_cliente, name='actualizar_datos_cliente'),

    path('lectura/', lecturas_view, name="lectura"),
    path('pagos/', pagos_view, name="pagos"),
]
