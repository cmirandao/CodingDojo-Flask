from datetime import date, datetime
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = '@#SSDS%^&G' 

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    # print(request.form)
    session['frutilla'] = request.form['strawberry']
    session['frambuesa'] = request.form['raspberry']
    session['manzana'] = request.form['apple']
    session['mora'] = request.form['blackberry']
    session['nombre'] = request.form['first_name']
    session['apellido'] = request.form['last_name']
    session['identificacion'] = request.form['student_id']
    
    return redirect("/agradecimiento")

@app.route("/agradecimiento", methods=['GET'])
def gracias_por_comprar():
    suma=0
    frut1=int(session['frutilla'])
    frut2=int(session['mora'])
    frut3=int(session['manzana'])
    frut4=int(session['frambuesa'])
    suma=frut1+frut2+frut3+frut4
    fecha=datetime.today().strftime('%A, %B %d %Y - %H:%M:%S')
    print("manzanas: ",session['manzana'])
    print("moras: ",session['mora'])
    print("frambuesas: ",session['frambuesa'])
    print("frutillas: ",session['frutilla'])
    print("Cobrando a ",session['nombre']," ",session['apellido']," por ",suma," frutas.")
    return render_template("checkout.html",suma=suma,fecha=fecha)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    