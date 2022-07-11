
from django.urls import path
from MoniApp import views



urlpatterns = [

    path('home/', views.home, name="home"),
    path('crearForm/',views.crearForm, name = 'crearForm'),
    path('listado/', views.listado, name="listado"),
    path('actualizar/', views.actualizar, name="actualizar_action"),
    path('actualizar/<identificador>/', views.actualizar, name="actualizar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),

]
