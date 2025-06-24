from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_parroquias_y_barrios, name='inicio'),  
    path('parroquias/', views.listar_parroquias_y_barrios, name='listar_parroquias_y_barrios'),
    path('barrios/', views.listar_barrios, name='listar_barrios'),
    path('crear-parroquia/', views.crear_parroquia, name='crear_parroquia'),
    path('crear-barrio/', views.crear_barrio, name='crear_barrio'),
]
