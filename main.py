from flask import Flask, render_template

app=Flask(__name__)

@app.route("/")
def index():
    titulo = "IGS805"
    lista=["Pedro", "Juan", "Mario"]
    return render_template("index.html", titulo=titulo, lista=lista)

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

if __name__=="__main__":
    app.run(debug=True, port=3000)