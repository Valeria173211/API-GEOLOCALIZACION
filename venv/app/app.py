from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicio():
    return render_template("index.html", seccion="Inicio")

@app.route("/importancia")
def importancia():
    return render_template("index.html", seccion="Importancia")

@app.route("/gestion")
def gestion():
    return render_template("index.html", seccion="Gestión Ambiental")

@app.route("/futuro")
def futuro():
    return render_template("index.html", seccion="Futuras Generaciones")

@app.route("/3r")
def tresr():
    return render_template("index.html", seccion="3R")

if __name__ == "__main__":
    app.run(debug=True)
