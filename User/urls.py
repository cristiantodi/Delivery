from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    # path('cliente/', views.vista_cliente, name='vista_cliente'),
    # path('delivery/', views.vista_mensajero, name='vista_mensajero'),
    path('registro/', views.registro_cliente, name='registro_cliente'),
]