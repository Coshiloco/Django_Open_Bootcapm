# Importamos render parecido a los de las vistas de express
from django.shortcuts import render

# Generamos la view que es la logica de lo que va a ver el usuario de simple


def simple(request):
    return render(request=request, template_name='simple.html', context={})


# Vamos a poner contenido dinamico en el html con esta View

def plantilladinamica(request, nombreusuario):
    categories = ["web", "frontend", 78]
    context = {"nombreusuario": nombreusuario, "categories": categories}
    return render(request=request, template_name='dinamico.html', context=context)
