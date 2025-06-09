from django.shortcuts import render
from .models import Plato

# Create your views here.


def menu(request):
    platos = Plato.objects.filter(disponible=True)
    return render(request, 'menu.html', {'platos': platos})