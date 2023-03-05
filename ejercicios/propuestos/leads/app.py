"""
Nombre del programa:
Descripción:
Autor del programa: Rafael Jiménez Cobos
Fecha de creación: 11/2/23
"""

from flask import Flask, request, render_template
import pickle
import numpy as np
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__, template_folder="./html")


@app.route('/html')
def inicio():
    return render_template("./data_form1.html")


@app.route('/html/data_form2', methods=['POST'])
def data_form2():
    list1 = []
    for num in range(14):
        if isinstance(request.form[f'pregunta{num}'], str):
            if "." in request.form[f'pregunta{num}']:
                value = float(request.form[f'pregunta{num}'])
            else:
                value = int(request.form[f'pregunta{num}'])

            if num == 1 or num == 3:
                value = float(request.form.get(f'pregunta{num}'))

            list1.append(value)

    return render_template("./data_form2.html", list=list1)


@app.route('/html/data_form3', methods=['POST'])
def data_form3():
    lista_anterior = request.form.get('list1')
    lista_anterior = lista_anterior.strip('][').split(', ')
    listado = []
    list2 = []

    for item in lista_anterior:
        if isinstance(item, str):
            if "." in item:
                valor = float(item)
            else:
                valor = int(item)
            listado.append(valor)

    for num in range(14):
        if isinstance(request.form[f'pregunta{num}'], str):
            if "." in request.form[f'pregunta{num}']:
                value = float(request.form[f'pregunta{num}'])
            else:
                value = int(request.form[f'pregunta{num}'])

            list2.append(value)

    lista_conjunta = listado + list2

    return render_template("./data_form3.html", list=lista_conjunta)


@app.route('/html/data_form4', methods=['POST'])
def data_form4():
    lista_anterior = request.form.get('list2')
    lista_anterior = lista_anterior.strip('][').split(', ')
    print(lista_anterior)
    listado = []
    list3 = []

    for item in lista_anterior:
        if isinstance(item, str):
            if "." in item:
                valor = float(item)
            else:
                valor = int(item)
            listado.append(valor)

    for num in range(14):
        if isinstance(request.form[f'pregunta{num}'], str):
            if "." in request.form[f'pregunta{num}']:
                value = float(request.form[f'pregunta{num}'])
            else:
                value = int(request.form[f'pregunta{num}'])

            list3.append(value)

    lista_conjunta = listado + list3

    return render_template("./data_form4.html", list=lista_conjunta)


@app.route('/html/prediction', methods=['POST'])
def prediction():
    lista_anterior = request.form.get('list3')
    lista_anterior = lista_anterior.strip('][').split(', ')
    listado = []
    list4 = []

    for item in lista_anterior:
        if isinstance(item, str):
            if "." in item:
                valor = float(item)
            else:
                valor = int(item)
            listado.append(valor)

    for num in range(14):
        if isinstance(request.form[f'pregunta{num}'], str):
            if "." in request.form[f'pregunta{num}']:
                value = float(request.form[f'pregunta{num}'])
            else:
                value = int(request.form[f'pregunta{num}'])

            list4.append(value)

    lista_conjunta = listado + list4

    valuesForPrediction = np.array(lista_conjunta)
    model = pickle.load(open('./model/leads_model.pkl', 'rb'))
    clientPrediction = model.predict(valuesForPrediction.reshape(1, -1))

    if clientPrediction == 0:
        result = False
    else:
        result = True

    return render_template("./prediction.html", result=result)


# Run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
