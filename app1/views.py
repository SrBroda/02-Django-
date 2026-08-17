from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def v1_app1(request):
    return HttpResponse("<h1>Vista 1 App1</h1>")

def v2_app2(request):
    return HttpResponse("<h1>Vista 2 App1</h1>"
    "<p>Todo lo que necesitas</p>")