from django.urls import path 
from . import views 

urlpatterns = [
    path('vista1/', views.v1_app1),
    path("vista2/", views.v2_app2)

]