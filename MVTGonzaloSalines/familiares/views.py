from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from familiares.models import MisFamiliares

# Create your views here.

def listado_familia(request):

    # Se obtienen los datos de la tabla Familiares
    listado_familia = MisFamiliares.objects.all()

    
    # Se genera un diccionario con la lista
    datos = {
        "listado_familia": listado_familia,

    }

    # Se obtiene el template html
    plantillas = loader.get_template("plantilla.html")
    
    # Se renderiza datos en la plantilla y se almacena en la variable documento
    documento =  plantillas.render(datos)
    
    # Retorna la variable documento
    return HttpResponse(documento)
