from django.http import HttpResponse


def inicio(request):
    # Esta vista responde cuando el usuario visita la página principal.
    return HttpResponse("<h1>Bienvenido al blog de Patrick Jane</h1>")


def lista_posts(request):
    # Más adelante los posts vendrán desde la base de datos.
    return HttpResponse("<h1>Listado de publicaciones</h1>")


def acerca_de_mi(request):
    # Esta vista muestra información sobre el autor del blog.
    return HttpResponse(
        "<h1>Acerca de mí</h1>"
        "<p>Soy Patrick Jane, consultor e investigador.</p>"
    )