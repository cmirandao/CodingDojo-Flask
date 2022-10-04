from app_encuesta_dojo import app
from flask import render_template,redirect, session, request
app.secret_key = '@#SSDS%^&G' 

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    session['nombre'] = request.form['nombre']
    session['locacion'] = request.form['locacion']
    session['lenguaje'] = request.form['lenguaje']
    session['comentario'] = request.form['txarea']
    return redirect('/result')

@app.route('/result', methods=['GET'])
def result():
    nombre=session['nombre']
    locacion=session['locacion']
    lenguaje=session['lenguaje']
    comentario=session['comentario']
    return render_template('result.html',nombre=nombre,locacion=locacion,lenguaje=lenguaje,comentario=comentario)

@app.route('/volver')
def volver():
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404