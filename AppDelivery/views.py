from django.shortcuts import render
from Menu.models import Plato
# Create your views here.

def Home(request):
    platos = Plato.objects.filter(disponible=True)
    return render(request, 'home.html', {'platos': platos})