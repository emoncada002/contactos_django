from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_contactos, name='lista_contactos'),
    path('crear/', views.crear_contacto, name='crear_contacto'),
    path('editar/<int:pk>/', views.editar_contacto, name='editar_contacto'),
    path('eliminar/<int:pk>/', views.eliminar_contacto, name='eliminar_contacto'),
    path('exportar_csv/', views.exportar_contactos_csv, name='exportar_contactos_csv'),
]
