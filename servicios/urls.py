from django.urls import path, include
from rest_framework import routers
from . import views
from .views import contacto_view

# Definir el router para la API
router = routers.DefaultRouter()
router.register(r'servicios', views.ServicioViewSet)
router.register(r'proyectos', views.ProyectoViewSet) 

urlpatterns = [
    # URLs de la API
    path('api/', include(router.urls)),
    
    # URLs para las vistas del sitio web
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('services/', views.services, name='services'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('contacto/', contacto_view, name='contacto'),
]
