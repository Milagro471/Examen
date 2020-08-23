from flask import Flask, jsonify, request
from To_Do import ListTo_Do

app = Flask(__name__)

#Entregar Datos JSON (Get:Obtener Datos, Post:Guardar Datos, Put: Actualizar, Delete: Borrar)
@app.route('/ping')#GET por defecto
def ping():
    return jsonify({"message": "Pong!"})

#toda la lista
@app.route('/ListTo_Do')
def getList():
    return jsonify({"Lista de Cosas por Hacer": ListTo_Do})


#Solo uno
@app.route('/ListTo_Do/<string:tarea>')
def getLista(tarea):
    tareaFound = [ListTareas for ListTareas in ListTo_Do if ListTareas['Tarea'] == tarea] #Recorre la lista
    if(len(tareaFound) > 0): #validacion para que no se caiga
        return jsonify({"ListTarea": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})

#(app insomnia->Permite enviar y mostrar Datos a nuestras Rest API)

#Crear y agregar Datos
@app.route('/ListTo_Do', methods=['POST'])
def addTarea():
    new_tarea = {
        "Tarea": request.json['Tarea'],
        "Dia": request.json['Dia'],
        "Hora": request.json['Hora']
    }
    ListTo_Do.append(new_tarea)
    return jsonify({"Message": "Tarea Agregada...!!!", "Lista de Cosas por Hacer": ListTo_Do})

#Actualizar Datos
@app.route('/ListTo_Do/<string:tarea>', methods=['PUT'])
def editTarea(tarea):
    tareaFound = [ListTareas for ListTareas in ListTo_Do if ListTareas['Tarea'] == tarea]    
    if(len(tareaFound) > 0):
        tareaFound[0]['Tarea'] = request.json['Tarea']
        tareaFound[0]['Dia'] = request.json['Dia']
        tareaFound[0]['Hora'] = request.json['Hora']
        return jsonify({"Message": "Tarea Actualizada","Lista de Tareas": tareaFound[0]})
    return jsonify({"Message": "Tarea No encontrada..."})

    #Eliminar Datos
    @app.route('/ListTo_Do/<string:tarea>', methods=['DELETE'])
    def deleteTarea(tarea):
        tareaFound = [ListTareas for ListTareas in ListTo_Do if ListTareas['Tarea'] == tarea]    
        if(len(tareaFound) > 0):
            ListTo_Do.remove(tareaFound[0])
            return jsonify({"Message": "Tarea Eliminada...","Lista de Tareas": ListTo_Do })
        return jsonify({"Message": "Tarea No encontrada..."})

if __name__ == '__main__':
    app.run(debug=True, port=4000)