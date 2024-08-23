from django.shortcuts import render
from django.http import HttpResponse
from AppEntrega3.models import Registro, Ubicacion, Pelicula

# Create your views here.

def inicio(req):
    return render(req, 'appentrega3/padre.html')

def registro(req):
     return render(req, 'appentrega3/registro.html')

def ubicacion(req):
     return render(req, 'appentrega3/ubicacion.html')

def pelicula(req):
   return render(req, 'appentrega3/pelicula.html')



def registro_Formulario(req):

    if req.method == 'POST':
        registro = Registro(nombre=req.POST['nombre'], apellido=req.POST['apellido'], email=req.POST['email'], edad=req.POST['edad'])
        registro.save()


        return render(req, 'AppEntrega3/padre.html')
    



def ubicacion_Formulario(req):

    if req.method == 'POST':
        ubicacion = Ubicacion(ciudad=req.POST['ciudad'], capital=req.POST['capital'], codigo_postal=req.POST["codigo_posta"])
        ubicacion.save()


        return render(req, 'AppEntrega3/ubicacion.html')
    
   

def pelicula_Formulario(req):

    if req.method == 'POST':
        pelicula = Pelicula(nombre=req.POST['nombre'], genero=req.POST['genero'], año=req.POST['año'])
        pelicula.save()


        return render(req, 'AppEntrega3/pelicula.html')
    



def busca_Informacion(req):
    return render  (req, "AppEntrega3/buscar_informacion.html")
    

def buscar(req):
    if req.GET.get("nombre"):  # Obtener el nombre del campo de entrada
        nombre = req.GET["nombre"]
        registros = Registro.objects.filter(nombre__icontains=nombre)  # Filtrar registros que contienen el nombre

        return render(req, "AppEntrega3/padre.html", {
            "registros": registros,
            "nombre": nombre
        })
    else:
        return render(req, "AppEntrega3/padre.html")

        
    
   
