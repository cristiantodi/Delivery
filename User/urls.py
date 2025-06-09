from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_usuario, name='login'),
    path('logout/', views.logout_usuario, name='logout'),
    path('cliente/', views.vista_cliente, name='vista_cliente'),
    path('delivery/', views.vista_mensajero, name='vista_mensajero'),
]