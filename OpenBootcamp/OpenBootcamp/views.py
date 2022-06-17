# Importamos la libreria que se nos autoimporto
from django.http import HttpResponse

# Hola mundo Django


def saludo(request):
    return HttpResponse("Hola Mundo Soy Django")


# View de Despedida que se enlaza con urls.py

def despedida(request):
    return HttpResponse("Soy Otro circuito de Views Y La despedida")


# View de prueba de url con parametro asociada a la url publicacionforo/<str:id>/ donde lo que va entre <parametro>
# Le sugundo parametro tiene el nombre de como se guarda en la url que en este caso es id

def publicacionforo(request, id):
    return HttpResponse(f"El parametro que escribimos en la url ha pasado ha esta funcion y es {id}")
