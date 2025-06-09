from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_pedido, name='crear_pedido'),
    path('seguimiento/<int:pedido_id>/', views.seguimiento_pedido, name='seguimiento_pedido'),
    path('actualizar_ubicacion/', views.actualizar_ubicacion, name='actualizar_ubicacion'),
]
