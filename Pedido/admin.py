from django.contrib import admin
from .models import Pedido

# Register your models here.

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'plato', 'estado', 'mensajero', 'fecha')
    list_filter = ('estado', 'fecha')
    search_fields = ('cliente__username', 'plato__nombre', 'mensajero__username')
    autocomplete_fields = ['cliente', 'mensajero']