

from django.views.decorators.csrf import csrf_exempt
from json import JSONDecodeError
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Cliente


def inicio_view(request):
    return render(request, 'base.html')

def añadir_clientes_view(request):
    return render(request, 'añadir_clientes.html')



@csrf_exempt
def insertar_cliente(request):
    try:
        if request.method == 'POST':
            data = request.POST  # Utiliza request.POST para obtener datos del formulario
            rut = data.get('rut')
            nombre = data.get('nombre')
            apellido = data.get('apellido')
            sector = data.get('sector')
            estado = data.get('estado')
            tipo_usuario = data.get('tipo_usuario')

            cliente = Cliente(rut=rut, nombre=nombre, apellido=apellido, sector=sector, estado=estado, tipo_usuario=tipo_usuario)
            cliente.save()


            return redirect('añadir_clientes')
        else:
            return JsonResponse({'error': 'Método no permitido.'})
    except JSONDecodeError:
        return JsonResponse({'error': 'Error al decodificar el JSON en el cuerpo de la solicitud.'})






from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Cliente

def modificar_clientes_view(request):
    return render(request, 'modificar_clientes.html')


@csrf_exempt
def actualizar_datos_cliente(request):
    try:
        if request.method == 'POST':
            data = request.POST
            rut_cliente = data.get('rut_cliente')
            nuevo_apellido = data.get('nuevo_apellido')
            nuevo_sector = data.get('nuevo_sector')
            nuevo_estado = data.get('nuevo_estado')
            nuevo_tipo_usuario = data.get('nuevo_tipo_usuario')

            # Actualizar los datos del cliente en la base de datos
            cliente = Cliente.objects.get(rut=rut_cliente)
            cliente.apellido = nuevo_apellido
            cliente.sector = nuevo_sector
            cliente.estado = nuevo_estado
            cliente.tipo_usuario = nuevo_tipo_usuario
            cliente.save()

            # Después de la actualización, redireccionar a la vista de modificar_clientes
            return redirect('modificar_clientes')
        else:
            return JsonResponse({'error': 'Método no permitido.'})
    except Exception as e:
        return JsonResponse({'error': str(e)})









def ver_clientes_activos_view(request):
    # Obtener la lista de sectores para cargar en el formulario
    sectores = Cliente.objects.values_list('sector', flat=True).distinct()

    # Verificar si es una solicitud POST (formulario enviado)
    if request.method == 'POST':
        # Obtener el sector seleccionado en el formulario
        selected_sector = request.POST.get('searchSelect')

        # Realizar la búsqueda de clientes activos que coincidan con el sector seleccionado
        clientes_activos = Cliente.objects.filter(estado='Activo', sector=selected_sector)

        # Renderizar la página con la lista de sectores y los resultados de la búsqueda
        context = {'sectores': sectores, 'resultados': clientes_activos}
        return render(request, 'ver_clientes_activos.html', context)

    # Si es una solicitud GET, simplemente renderizar la página con la lista de sectores
    context = {'sectores': sectores}
    return render(request, 'ver_clientes_activos.html', context)


def filtrar_clientes_por_sector(request):
    # Obtener el sector seleccionado en el formulario
    selected_sector = request.GET.get('searchSelect')

    # Realizar la búsqueda de clientes activos que coincidan con el sector seleccionado
    clientes_activos = Cliente.objects.filter(estado='Activo', sector=selected_sector)

    # Crear una lista de diccionarios con la información de los clientes para enviar como respuesta JSON
    resultados = []
    for cliente in clientes_activos:
        resultados.append({
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'sector': cliente.sector,
        })

    return JsonResponse({'resultados': resultados})



def mostrar_todos_clientes_activos(request):
    # Obtén todos los clientes activos
    clientes_activos = Cliente.objects.filter(estado='Activo')

    # Crear una lista de diccionarios con la información de los clientes para enviar como respuesta JSON
    resultados = []
    for cliente in clientes_activos:
        resultados.append({
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'sector': cliente.sector,
        })

    return JsonResponse({'resultados': resultados})



def mostrar_todos_clientes_inactivos(request):
    # Obtén todos los clientes activos
    clientes_inactivos = Cliente.objects.filter(estado='Inactivo')

    # Crear una lista de diccionarios con la información de los clientes para enviar como respuesta JSON
    resultados = []
    for cliente in clientes_inactivos:
        resultados.append({
            'rut': cliente.rut,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'sector': cliente.sector,
        })

    return JsonResponse({'resultados': resultados})



def ver_clientes_inactivos_view(request):
    # Obtener la lista de sectores para cargar en el formulario
    sectores = Cliente.objects.values_list('sector', flat=True).distinct()

    # Verificar si es una solicitud POST (formulario enviado)
    if request.method == 'POST':
        # Obtener el sector seleccionado en el formulario
        selected_sector = request.POST.get('searchSelect')

        # Realizar la búsqueda de clientes inactivos que coincidan con el sector seleccionado
        clientes_inactivos = Cliente.objects.filter(estado='Inactivo', sector=selected_sector)

        # Renderizar la página con la lista de sectores y los resultados de la búsqueda
        context = {'sectores': sectores, 'resultados': clientes_inactivos}
        return render(request, 'ver_clientes_inactivos.html', context)

    # Si es una solicitud GET, simplemente renderizar la página con la lista de sectores
    context = {'sectores': sectores}
    return render(request, 'ver_clientes_inactivos.html', context)







def añadir_clientes_view(request):
    return render(request, 'añadir_clientes.html')



def lecturas_view(request):
    return render(request, 'lectura.html')

def pagos_view(request):
    return render(request, 'pagos.html')







def buscar_cliente_por_rut(request):
    if request.method == 'GET':
        rut = request.GET.get('rut', None)

        # Buscar el cliente por Rut en la base de datos
        try:
            cliente = Cliente.objects.get(rut=rut)
            cliente_info = {
                'rut': cliente.rut,
                'nombre': cliente.nombre,
                'apellido': cliente.apellido,
                'sector': cliente.sector,
                'estado': cliente.estado,
                'tipo_usuario': cliente.tipo_usuario,
            }
            return JsonResponse({'cliente_encontrado': True, 'cliente': cliente_info})
        except Cliente.DoesNotExist:
            return JsonResponse({'cliente_encontrado': False})
