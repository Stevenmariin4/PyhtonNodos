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
    return jsonify({'Nombre': 'Nodo Uno', 'Total': total})


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
        valorNodo.append({'Nombre': 'Nodo Uno', 'Total': total})
        sumaTotal = 0
        sumaTotal = sumaTotal + total
        for vecino in vecinos:
            respuesta = requests.get(vecino)
            jsonRespuesta = json.loads(respuesta.content)
            if(len(jsonRespuesta['Resultado']) > 0):
                sumaTotal = sumaTotal + jsonRespuesta['Total']
                valorNodo.append(jsonRespuesta)
        return jsonify({'Resultado': valorNodo, "Total": sumaTotal})
    else:
        return jsonify({'Resultado': []})


if __name__ == "__main__":
    app.run(debug=True, port=1000, host="0.0.0.0")
