from django.http import HttpResponse 

def inicio(request): 
    nombre = "miguel cepeda"
    return HttpResponse(f"¡Bienvenidos a mi primera app Django, {nombre}!")