from django.urls import path 
from . import views 

urlpatterns = [
    path('vista1/', views.v1_Inicio),
    path("vista2/", views.v2_Inicio)

]