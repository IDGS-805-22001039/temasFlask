from flask import Flask, render_template, request
from io import open
import os
import forms


app=Flask(__name__)

class Cine:
    def __init__(self, boletos, compradores, nombre):
        self.boletos = boletos
        self.compradores = compradores
        self.nombre = nombre
        self.boleto = 12
        self.total = 0.0
    
    def sin_descuento(self):
        self.total = self.boletos * self.boleto
        return f"En total pagarás ${self.total}"

    def descuento_10(self):
        self.total = self.boletos * self.boleto
        self.total -= self.total * 0.10
        return self.total
    
    def descuento_cineco(self):
        self.total -= self.total * 0.10
        return self.total
    
    def descuento_15(self):
        self.total = self.boletos * self.boleto
        self.total -= self.total * 0.15
        return self.total

    def guardar_compra(self):
        if self.compradores == 1:
            texto = f"\n{self.nombre} compró {self.boletos} boletos por una cantidad de ${self.total}"
        else:
            texto = f"\n{self.nombre} y sus {self.compradores} acompañantes compraron {self.boletos} boletos por una cantidad de ${self.total}"

        with open('registro.txt', 'a') as fichero:
            fichero.write(texto)

    def imprimir_ticket(self):
        with open('registro.txt', 'r') as fichero:
            texto = fichero.read()
        print

@app.route("/")
def index():
    titulo = "IGS805"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/alumnos", methods = ["GET", "POST"])
def alumnos():
    mat=""
    nom=""
    ape=""
    email=""
    alumno_clase=forms.UserForm(request.form)
    if request.method=="POST":
        mat = alumno_clase.matricula.data
        nom = alumno_clase.nombre.data
        ape = alumno_clase.Apellido.data
        email = alumno_clase.email.data
        print('Nombre: {}'.format(nom)) 
    return render_template("Alumnos.html", form=alumno_clase)   
    

@app.route("/ejemplo1")
def ejmeplo1():
    return render_template("ejemplo1.html")

@app.route("/ejemplo2")
def ejmeplo2():
    return render_template("ejemplo2.html")

@app.route("/user/<string:user>")
def use(user):
    return f"hola {user}"

@app.route("/Hola")
def hola():
    return "Hola México"

@app.route("/numero/<int:num>")
def numero(num):
    return f"El numero es {num}" 

@app.route("/user/<int:id>/<string:username>")
def username(user, id):
    return f"El usuario es: {user}, con id:{id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    resp = n1 + n2
    return f"{n1} + {n2} = {resp}"

@app.route("/default")
@app.route("/default/<string:tem>")
def func1(tem='Juan'):
    return f"Hola {tem}"

@app.route("/form1")
def form1():
    return '''
            <form>
                <label for= "nombre">Nombre: </label>
                <input type="text" id="nombre" name="nombre"></input> <br><br>
                <label for= "nombre">Nombre: </label>
                <input type="text" id="nombre" name="nombre"></input> <br><br>
            </form>

            '''

@app.route('/OperasBas')
def oepras():
    return render_template("OperasBas.html")

@app.route('/resultado1', methods = ["GET", "POST"])
def resultado1():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        rest = int(num1) * int(num2)

        return "La multiplicación de {} x {} = ".format(num1,num2)
    
@app.route('/cineco')
def cienco():
    return render_template("cinepolis.html")

@app.route('/comprarBoletos', methods=["POST"])
def comprarBoletas():
    nombre = request.form.get("nombre")
    compradores = int(request.form.get("compradores"))
    tarjeta_cineco = int(request.form.get("cineco"))
    boletos = int(request.form.get("cantidad"))

    limite = compradores * 7
    if boletos > limite:
        error_message = "Acción requerida: El número de boletos sobrepasa el límite permitido de comprar por comprador."
        return render_template('cinepolis.html', error=error_message)

    cine = Cine(boletos, compradores, nombre)
    if boletos > 0 and boletos <= 2:
        cine.sin_descuento()
    elif boletos >= 3 and boletos <= 5:
        cine.descuento_10()
    elif boletos > 5:
        cine.descuento_15()

    if tarjeta_cineco == 1:
        cine.descuento_cineco()

    cine.guardar_compra()
    total = cine.total

    return render_template('cinepolis.html', total=total)

if __name__=="__main__":
    app.run(debug=True, port=3000)