from django.shortcuts import render, redirect
from django.shortcuts import render

# importar las clases de models.py
from proyectoUno.models import *

# importar los formularios de forms.py
from proyectoUno.forms import *

# Create your views here.

def index(request): 
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numEdificios': len(edificios)}
    return render(request, 'index.html', informacion_template)


def obtenerEdificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    informacion_template = {'edificio': edificio}
    return render(request, 'obtenerEdificio.html', informacion_template)

# Métodos para CRUD de Edificio
def agregarEdificio(request):

    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() 
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'agregarEdificio.html', diccionario)


def editarEdificio(request, id):

    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editarEdificio.html', diccionario)


def eliminarEdificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

# Métodos para CRUD de Departamento

def agregarDepartamento(request):

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'agregarDepartamento.html', diccionario)


def editarDepartamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editarDepartamento.html', diccionario)

def eliminarDepartamento(request, id):
    departamento= Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

def agregarDepartamentoEdificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoEdificioForm(edificio, request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoEdificioForm(edificio)
    diccionario = {'formulario': formulario, 'edificio': edificio}

    return render(request, 'agregarDepartamentoEdificio.html', diccionario)
