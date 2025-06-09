from django.db import models
from User.models import Usuario
from Menu.models import Plato

# Create your models here.

class EstadoPedido(models.Model):
    estado = models.CharField(max_length=50)
    # RECIBIDO = 'recibido', 'Pedido Recibido'
    # PREPARANDO = 'preparando', 'Preparando'
    # EN_CAMINO = 'en_camino', 'En camino'
    # ENTREGADO = 'entregado', 'Entregado'

class Pedido(models.Model):
    cliente     = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='pedidos_cliente')
    mensajero   = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos_mensajero')
    plato       = models.ForeignKey(Plato, on_delete=models.CASCADE)
    drc_entrega = models.CharField(max_length=255)
    estado      = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, max_length=50)
    fecha       = models.DateTimeField(auto_now_add=True)
    gps_mensajero = models.CharField(max_length=255, blank=True, null=True)  # Ej: "4.6097,-74.0817"

    def __str__(self):
        return f"Pedido #{self.id} - {self.estado}"