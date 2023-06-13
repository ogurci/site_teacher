from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'main'),
    path('predmet1', views.predmet1, name = 'predmet1'),
    path('theory1', views.theory1, name = 'theory1'),
    path('practica1', views.practica1, name='practica1'),
    path('predmet2', views.predmet2, name = 'predmet2'),
    path('theory2', views.theory2, name = 'theory2'),
    path('practica2', views.practica2, name='practica2')
]