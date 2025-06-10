from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .forms import RegistroClienteForm

# Create your views here.

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('Home')  # o redirige según tipo de usuario
        else:
            return render(request, 'login.html', {'error': 'Usuario o contraseña incorrectos'})
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

def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('Home')  # Redirige a la página de inicio o donde desees
    else:
        form = RegistroClienteForm()
    return render(request, 'registro_cliente.html', {'form': form})