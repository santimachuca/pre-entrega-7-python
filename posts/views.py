from django.shortcuts import render


def inicio(request):
    # Muestra la plantilla de la página principal.
    return render(request, "posts/inicio.html")


def lista_posts(request):
    # Lista temporal: más adelante vendrá desde la base de datos.
    posts = [
        {
            "titulo": "El misterio de la mansión",
            "contenido": "Patrick encontró una pista importante.",
        },
        {
            "titulo": "Las pistas de Red John",
            "contenido": "Una nueva investigación comienza en el CBI.",
        },
        {
            "titulo": "El arte de observar",
            "contenido": "Los pequeños detalles pueden resolver un caso.",
        },
    ]

    # El contexto transporta información desde Python hacia el template.
    contexto = {
        "posts": posts,
    }

    # Envía el contexto a lista_posts.html.
    return render(request, "posts/lista_posts.html", contexto)


def acerca_de_mi(request):
    # Muestra la plantilla con información sobre el autor.
    return render(request, "posts/acerca_de_mi.html")