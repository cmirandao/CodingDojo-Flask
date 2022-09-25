from app_patio_juegos import app
from flask import render_template

@app.route('/')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente 
def hola_mundo():                   # y a menos que no indiquemos otro metodo de consulta, es por default GET
    return 'Hola Mundo!'  # Devuelve la cadena '¡Hola Mundo!' como respuesta

@app.route('/play')
def prisma():
    return render_template('jugar.html', numero=3, color="lightblue")

@app.route('/play/<int:numero>')
def num_prisma(numero):
    return render_template('jugar.html', numero=numero, color="lightblue")

@app.route('/play/<int:numero>/<color>')
def repetir_prisma(numero, color):
    return render_template('jugar.html', numero=numero, color=color)

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404