from crypt import methods
from email import message
from app_oro_ninja import app
import random
from datetime import datetime
from flask import render_template, request, redirect, session 
app.secret_key = '@#SSDS%^&G'

@app.route('/')
def inicio():
    # session['visible']="hidden"
    # session['visi_ble']=""
    return render_template("index.html",mensajes=session['msj'],tu_oro=session['your_gold'],visible1=session['visible'],visible2=session['visi_ble'])
def crear_rnds():
    cont=0
    session['cont']=cont
    your_gold=0
    session['your_gold']=your_gold
    color="black"
    session['color']=color
    visible1="hidden"
    visible2=""
    session['visible']=visible1
    session['visi_ble']=visible2
    
    if 'msj' not in session:
        session['msj']=[]
    return inicio()


@app.route('/process_money',methods=['GET','POST'])
def proceso():
    ccnntt=int(session['cont'])
    fecha=datetime.today().strftime('%A, %B %d %Y - %H:%M:%S')
    mas_menos=random.randint(1,2) # 1:suma, 2:resta
    farm=random.randint(10,20)
    cave=random.randint(5,10)
    house=random.randint(2,5)
    casino=random.randint(0,50)
    valor=request.form['building']
    mi_oro=int(session['your_gold'])
    color=session['color']
    visible1=session['visible']
    visible2=session['visi_ble']
    lugares=[
    {'lugar':'farm','gold':farm},
    {'lugar':'cave','gold':cave},
    {'lugar':'house','gold':house},
    {'lugar':'casino','gold':casino}
    ]
    if ccnntt<15:
        for lugar in lugares:
            if valor==lugar['lugar']:
                visible1="hidden"
                visible2=""
                print("oro: ",mi_oro)
                if mi_oro>=500:
                    visible1=""
                    visible2="hidden"
                    lista=session['msj']
                    lista.insert(0,{'mensj':"<li style='list-style:none;'>Felicidades ganaste 500 monedas en menos de 15 movimientos</li>"})
                elif mas_menos==1:
                    mi_oro+=lugar['gold']
                    color="green"
                    lista=session['msj']
                    lista.insert(0,{'mensj':"<li style='color: "+color+";list-style:none;'>Earned "+str(lugar['gold'])+" golds from the "+str(lugar['lugar'])+"! ("+str(fecha)+")</li>"})
                else:
                    mi_oro-=lugar['gold']
                    color="red"
                    lista=session['msj']
                    lista.insert(0,{'mensj':"<li style='color: "+color+";list-style:none;'>Entered a "+str(lugar['lugar'])+" and lost "+str(lugar['gold'])+" golds... Ouch.. ("+str(fecha)+")</li>"})
                ccnntt+=1
    elif ccnntt>=15:
        visible1=""
        visible2="hidden"
        lista=session['msj']
        lista.insert(0,{'mensj':"<li style='list-style:none;'>Perdiste</li>"})
    
    session['your_gold']=mi_oro
    session['msj']=lista
    session['cont']=ccnntt
    session['color']=color
    session['visible']=visible1
    session['visi_ble']=visible2
    print("contador--> ",session['cont'])
    return redirect('/')

@app.route('/reiniciar')
def reiniciar():
    session['cont']=0
    session['msj']=[]
    session['your_gold']=0
    session['visible']="hidden"
    session['visi_ble']=""
    return redirect('/')

@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404