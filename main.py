from flask import Flask, request
from flask import json
from flask.json import jsonify, load
from numpy import character
from sqlalchemy.util.langhelpers import method_is_overridden
import src.funciones as f 
import numpy as np



"""
Acitavr el entorno: . <name of environment>/bin/activate
"""
app = Flask(__name__)

@app.route("/")
def inicio():
    return "Que pasa gente!!!!"

@app.route("/Autores")
def Autores():
    return f.Autores()

@app.route("/Frases")
def Frases():
    return f.Frases()

@app.route("/Especialida_principal_de_Autores")
def Campo():
    return f.Campo()

@app.route("/Frases/<name>")
def frase_Autor(name):
    pepe = f.frase_Autor(name)
    return f.limpia(pepe)

@app.route("/A_C")
def A_C():
    return f.A_C()


@app.route("/nuevo_campo", methods=["POST"])
def nuevo_campo():
    Campo = request.form.get("Campo")
    
    return f.insertar_Campo(Campo)

@app.route("/datos_autor", methods=["POST"])
def meter_datos():
    nombre = request.form.get("nombre")
    año_nacimiento =  request.form.get("año_nacimiento ")
    Campo = request.form.get("Campo")
    return f.insertar_datos_autor1(nombre, año_nacimiento, Campo )

@app.route("/insertar_frase", methods=["POST"])
def meter_frase():
    nombre = request.form.get("nombre")
    año_nacimiento =  request.form.get("año_nacimiento ")
    Campo = request.form.get("Campo")
    Frase = request.form.get("Frase")
    return f.insertar_frase(nombre, año_nacimiento, Campo, Frase )
















app.run(debug=True)
