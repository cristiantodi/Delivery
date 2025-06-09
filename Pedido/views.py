from django.shortcuts import render, redirect
from .models import Pedido, EstadoPedido
from Menu.models import Plato
from User.models import Usuario

# Create your views here.

def crear_pedido(request):
    plato_id = request.GET.get('plato')
    plato = Plato.objects.get(id=plato_id)
    pedido = Pedido.objects.create(cliente=request.user, plato=plato, direccion_entrega="Calle Ficticia 123")
    return redirect('seguimiento_pedido', pedido_id=pedido.id)

def seguimiento_pedido(request, pedido_id):
    pedido = Pedido.objects.get(id=pedido_id)
    return render(request, 'pedido/seguimiento.html', {'pedido': pedido})

def actualizar_ubicacion(request):
    import json
    data = json.loads(request.body)
    latlng = f"{data['lat']},{data['lng']}"
    pedido = Pedido.objects.filter(mensajero=request.user, estado='en_camino').last()
    if pedido:
        pedido.ubicacion_mensajero = latlng
        pedido.save()
    return redirect('vista_mensajero')
