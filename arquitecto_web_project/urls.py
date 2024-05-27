
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(('servicios.urls', 'servicios_api'))),  # Namespace para las rutas de la API
    path('', include(('servicios.urls', 'servicios_web'))),      # Namespace para las rutas del sitio web
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
