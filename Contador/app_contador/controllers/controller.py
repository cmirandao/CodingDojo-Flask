from app_contador import app
from flask import render_template, request, redirect, session 
app.secret_key = '@#SSDS%^&G'

@app.route('/')
def inicio():
    if 'cnt' in session:
        session['cnt']+=1
    else:
        session['cnt']=1
    return render_template("index.html")

@app.route("/dbl_visit")
def db_vst():
    session['cnt']+=1
    return redirect('/')

@app.route("/visitas", methods=['POST'])
def vst():
    session['nueva_cnt'] = request.form['cant_visitas']
    return redirect("/suma_visitas")

@app.route("/suma_visitas", methods=['GET'])
def sum_vst():
    nueva_cant=int(session['nueva_cnt'])
    session['cnt']+=nueva_cant-1
    return redirect('/')

@app.route('/destroy_session')
def rst():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404