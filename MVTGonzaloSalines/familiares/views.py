from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from familiares.models import MisFamiliares

# Create your views here.

def listado_familia(request):
    
    listado_familia = MisFamiliares.objects.all()    
    
    tabla = {
        "listado_familia": listado_familia
    }
    
    template = loader.get_template("plantilla.html")
    
    documento =  template.render(tabla)
        
    return HttpResponse(documento)
