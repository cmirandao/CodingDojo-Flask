import math
from app_ajedrez import app
from flask import render_template

# numero1:filas, numero2:columnas
@app.route('/')
def inicio():
    return render_template('index.html', numero1=8, numero2=8, color=1)

@app.route('/<int:numero>')
def tablero1(numero):
    return render_template('index.html', numero1=numero, numero2=8, color=1)

'''Se crea la variable color que indica si recibe o no parametros de color en la ruta
color=1 -> no recibe, color=2 -> recibe'''

@app.route('/<int:numero1>/<int:numero2>')
def tablero2(numero1,numero2):
    return render_template('index.html', numero1=numero1, numero2=numero2, color=1)

@app.route('/<int:numero1>/<int:numero2>/<color1>/<color2>')
def tablero3(numero1,numero2,color1,color2):
    return render_template('index.html', numero1=numero1, numero2=numero2, color1=color1, color2=color2,color=2)

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404