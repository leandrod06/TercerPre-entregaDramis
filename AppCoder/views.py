from django.http import HttpResponse
from django.shortcuts import render
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario


# Create your views here.
def curso(self):
    curso = Curso(nombre='Desarrollo Web', camada='19881')
    curso.save()

    documentodeTexto=f'--->Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(documentodeTexto)

def inicio(request):
    return render(request, 'AppCoder/inicio.html')

def curso(request):
    return render(request, 'AppCoder/cursos.html')

def profesores(request):
    return render(request, 'AppCoder/profesores.html')

def estudiantes(request):
    return render(request, 'AppCoder/estudiantes.html')

def entregables(request):
    return render(request, 'AppCoder/entregables.html')

from .forms import CursoFormulario

def cursoFormulario(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():  # Agrega paréntesis después de "is_valid"
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion['curso'], camada=informacion['camada'])  # Accede a los datos utilizando el diccionario "informacion"
            curso.save()
            return render(request, "AppCoder/inicio.html")
    else:
        miFormulario = CursoFormulario()  # Utiliza el nombre de la clase de formulario "CursoFormulario"

    return render(request, "AppCoder/cursos.html", {"miFormulario": miFormulario})

def busquedaCamada(request):
    return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):

    if request.GET["camada"]:
        #respuesta=f"Estoy buscando la camada nro: {request.GET['camada']}"
        camada=request.GET['camada']
        cursos=Curso.objects.filter(camada_icontains=camada)
        return render(request, "AppCoder/resultadosBusqueda.html", {"cursos":cursos, "camada":camada})
    else:
        respuesta="No enviaste datos"
    #No olvidar from django.http import HttpResponse
    return HttpResponse(respuesta)