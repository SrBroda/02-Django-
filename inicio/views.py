from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def v1_Inicio(request):
    return HttpResponse("<h1>Vista 1 Inicio</h1>")

def v2_Inicio(request):
    return HttpResponse("<h1>Vista 2 Inicio</h1>"
    "<p>Todo lo que necesitas</p>")

