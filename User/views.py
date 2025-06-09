from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Usuario

# Create your views here.

def login_usuario(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            if user.tipo == 'customer':
                return redirect('vista_cliente')
            return redirect('vista_mensajero')
    return render(request, 'login.html')

def logout_usuario(request):
    logout(request)
    return redirect('login')

def vista_cliente(request):
    return redirect('menu')

def vista_mensajero(request):
    from Pedido.models import Pedido
    pedidos = Pedido.objects.filter(estado='preparando', mensajero__isnull=True)
    return render(request, 'pedido/mensajero.html', {'pedidos': pedidos})