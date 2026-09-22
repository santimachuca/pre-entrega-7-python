from django.contrib import admin
from django.urls import include, path


# Rutas principales de todo el proyecto.
urlpatterns = [
    # Incluye las rutas creadas dentro de la aplicación posts.
    path("", include("posts.urls")),

    # Ruta del panel de administración de Django.
    path("admin/", admin.site.urls),
]