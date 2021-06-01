from flask import Flask, jsonify, request
from lista import lista, vecinos, statusresponse
import requests
import json
app = Flask(__name__)


@app.route('/listar', methods=['GET'])
def listarArray():
    total = 0
    for n in lista:
        total = total + n
    return jsonify({'Nombre': 'Nodo Cuatro', 'Total': total})


@app.route('/insertar', methods=['POST'])
def insertarArray():
    lista.append(request.json['numero'])
    return jsonify({'Operacion': 'Realizada'})


@app.route('/consultar', methods=['GET'])
def consultar():
    if(statusresponse['Status'] == False):
        statusresponse['Status'] = True
        total = 0
        for n in lista:
            total = total + n
        valorNodo = []
        valorNodo.append({'Nombre': 'Nodo Dos', 'Total': total})
        sumaTotal = 0
        sumaTotal = sumaTotal + total
        for vecino in vecinos:
            respuesta = requests.get(vecino)
            jsonRespuesta = json.loads(respuesta.content)
            if(len(jsonRespuesta['Resultado']) > 0):
                print(jsonRespuesta)
                for data in jsonRespuesta['Resultado']:
                    sumaTotal = sumaTotal + data['Total']
                    valorNodo.append(data)
        return jsonify({'Resultado': valorNodo, "Total": sumaTotal})
    else:
        return jsonify({'Resultado': [], "Total": 0})


@app.route('/reset')
def resetStatus():
    statusresponse['Status'] = False
    return jsonify({'Resulta': "Operacion Realizada"})


if __name__ == "__main__":
    app.run(debug=True, port=2000, host="0.0.0.0")
