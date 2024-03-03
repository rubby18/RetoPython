from flask import Flask, jsonify, request, json, url_for
import pandas as pd
app= Flask(__name__)
@app.route("/<matricula>")
def get_ultima_posicion(matricula):
    #Leer el fichero y devolver los datos del primer valor que coincida
    csv_data = pd.read_csv("./Ficheros/ordenadoPorFecha.csv", sep=",")
    jsonData=csv_data.to_json(orient="records")
    data = json.loads(jsonData)
    ultima_posicion={"Error":f"No disponemos de datos para la matricula {matricula}"}
    for vehiculo in data:
        if vehiculo["Matricula"]==matricula:
            ultima_posicion={"Matricula":matricula,"ultima_fecha":vehiculo["Pos_date"]}
            break
    return jsonify(ultima_posicion)

@app.route("/")
def inicio():
    return "API Caso 6"

if __name__=="__main__":
    app.run(debug=True)