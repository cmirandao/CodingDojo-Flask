from crypt import methods
from app_juego import app
import random
from flask import render_template, request, redirect, session 
app.secret_key = '@#SSDS%^&G'

@app.route('/')
def crear_rnd():
    numero_rnd=random.randint(1, 100)
    session['cnt']=numero_rnd
    cont=0
    session['cont']=cont
    return inicio(numero_rnd,cont,"","","hidden","hidden","","hidden")
def inicio(numero_rnd,cont, mensaje,color,visible,btn_visible,visible2,visible3):
    print("random: ",numero_rnd)
    print("contador: ",cont)
    return render_template('index.html',cont=cont,mensaje_solucion=mensaje,color=color,visible=visible,btn_visible=btn_visible,visible2=visible2,visible3=visible3)

@app.route('/adivinar',methods=['POST'])
def adivina():
    session['nuevo_valor']=request.form['num_guess']
    if int(session['cont'])<5:
        session['cont']+=1
    return redirect("/solucion")

@app.route('/solucion',methods=['GET'])
def solucion():
    num_rnd=int(session['cnt'])
    num_usuario=int(session['nuevo_valor'])
    cont=int(session['cont'])
    if num_rnd==num_usuario:
        mensaje_solucion="Correcto! El numero era "+str(session['cnt'])
        color="bg-success"
        visible=""
        btn_visible=""
        visible2="hidden"
        visible3=""
    elif num_usuario>num_rnd:
        mensaje_solucion="Muy alto!"
        color="bg-danger"
        visible=""
        btn_visible="hidden"
        visible2=""
        visible3="hidden"
    else:
        mensaje_solucion="Muy bajo!"
        color="bg-danger"
        visible=""
        btn_visible="hidden"
        visible2=""
        visible3="hidden"
    if cont==5 and num_rnd!=num_usuario:
        mensaje_solucion="Game Over - El numero era "+str(session['cnt'])
        color="bg-danger"
        visible=""
        btn_visible=""
        visible2="hidden"
        visible3="hidden"
    return inicio(num_rnd,cont, mensaje_solucion,color,visible,btn_visible,visible2,visible3)

@app.route('/registrar', methods=['POST'])
def registrar():
    session['nombre'] = request.form['nom_usr']
    session['apellido'] = request.form['ap_usr']
    return redirect("/marcador")

@app.route('/marcador',methods=['GET','POST'])
def marcador():
    if 'lista' not in session:
        session['lista']=[]
    if request.method=='GET':
        nomb=session['nombre']
        apll=session['apellido']
        cont=int(session['cont'])
        lista_lst=session['lista']
        lista_lst.append({'nom_usr' : nomb, 'ap_usr' : apll, 'cont' : cont})
        session['lista']=lista_lst
    # print(session['lista'])
    return render_template("marcador.html",usuarios=session['lista'])

@app.route('/ver_marcador')
def ver_marcador():
    return render_template("marcador.html",usuarios=session['lista'])

@app.route('/volver')
def volver():
    return redirect('/')

@app.route('/nuevo_juego')
def rst():
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404