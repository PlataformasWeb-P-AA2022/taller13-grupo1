from flask import Flask, render_template
import requests
import json
from config import user,contrasenia

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/")
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)




@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/")
    datos = json.loads(r.content)['results']
    numero_departamentos = json.loads(r.content)['count']
    datos2 = []
    for d in datos: 
        datos2.append({'propietario':d['propietario'], 'costo':d['costo'], 'numCuartos':d['numCuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentos.html", datos=datos2,
    numero_departamentos=numero_departamentos)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(user,contrasenia))
    nombre_edificio = json.loads(r.content)['nombre']
    cadena="%s %s " %(nombre_edificio)
    return cadena
