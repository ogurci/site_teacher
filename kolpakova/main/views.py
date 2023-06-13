from django.shortcuts import render
from .models import Teory1, Practic1, Nagrad, Teory2, Practic2

# Create your views here.
def index(request):
    file = Nagrad.objects.all()
    return render(request, 'main/index1.html', {'file': file})

def predmet1(request):
    return render(request, 'main/predmet1.html')

def theory1(request):
    file = Teory1.objects.all()
    return render(request, 'main/theory.html', {'file': file})

def practica1(request):
    file = Practic1.objects.all()
    return render(request, 'main/practica1.html', {'file': file})


def predmet2(request):
    return render(request, 'main/predmet2.html')

def theory2(request):
    file = Teory2.objects.all()
    return render(request, 'main/theory2.html', {'file': file})

def practica2(request):
    file = Practic2.objects.all()
    return render(request, 'main/practica2.html', {'file': file})

