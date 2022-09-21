from unittest import result
from flask import Flask
from flask import render_template
app = Flask(__name__)
'''--- Ejercicio 1 ---'''
@app.route('/')
def hola_mundo():
    return '¡Hola Mundo!'

'''--- Ejercicio 2 ---'''
@app.route('/dojo')
def dojo():
    return "¡Dojo!"

'''--- Ejercicio 3 - BONUS NINJA 1/BONUS SENSEI---'''
@app.route('/say/<string:name>')
def verificar(name):
    print (name)
    if name=="Flask" or name=="Juan" or name=="Michael" :
        return hola(name)
    else:
        return page_not_found(404)
    
def hola(newname):
    print(newname)
    return "Hola, " + newname

'''--- Ejercicio 4 - BONUS NINJA---'''
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/repeat/<int:number>/<palabra>')
def index(number,palabra):
    # result=(palabra+"\n")*number #imprime hacia el lado
    return render_template("index.html",palabra=palabra, number=number, result=result)

'''BONUS SENSEI'''
@app.errorhandler(404)
def page_not_found(e):
    return "¡Lo siento! No hay respuesta. Inténtalo otra vez.", 404

if __name__=="__main__": 
    app.run(debug=True)