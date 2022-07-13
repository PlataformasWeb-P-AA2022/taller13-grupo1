from django.shortcuts import render

# Create your views here.

def index(request): 
    """
        Listar los registros del modelo Estudiante,
        obtenidos de la base de datos.
    """
    edificios = Edificio.objects.all()
    informacion_template = {'edificios': edificios, 'numEdificios': len(edificios)}
    return render(request, 'index.html', informacion_template)
 