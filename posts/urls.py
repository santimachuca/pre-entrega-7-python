from django.urls import path

from . import views


# Estas rutas conectan cada dirección web con una vista.
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("posts/", views.lista_posts, name="lista_posts"),
    path("acerca-de-mi/", views.acerca_de_mi, name="acerca_de_mi"),
]