from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import Servicio, Proyecto
from .serializers import ServicioSerializer, ProyectoSerializer
from django.contrib import messages
from .forms import ContactoForm


# Vista para renderizar las plantillas HTML
def index(request):
    servicios = Servicio.objects.all()  # Asegúrate de que esto devuelva una lista
    proyectos = Proyecto.objects.all()  # Asegúrate de que esto devuelva una lista
    return render(request, 'index.html', {'servicios': servicios, 'proyectos': proyectos})

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def projects(request):
    return render(request, 'projects.html',{})

def services(request):
    return render(request, 'services.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def contacto_view(request):
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado exitosamente.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})
# ViewSet para la API
class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

