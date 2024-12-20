from django.http import HttpResponse
from django.shortcuts import render
from .models import Carta,Poema

def cartas(request):
    data={
        'cartas':Carta.objects.all()
    }
    return render(request, 'cartas.html',data)

def poemas(request):
    data={
        'poemas':Poema.objects.all()
    }
    return render(request, 'poema.html', data)