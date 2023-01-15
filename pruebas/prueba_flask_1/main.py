"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 15/1/23
"""

from flask import Flask, render_template, request

app = Flask(__name__, template_folder="./")


@app.route('/')
def inicio():
    return render_template("./formulario.html")


@app.route('/procesar', methods=['POST'])
def procesar():
    nombre = request.form.get("nombre")
    edad = request.form.get("edad")
    return render_template("./mostrar.html", nombre=nombre, edad=edad)


if __name__ == "__main__":
    app.run(debug=True)
