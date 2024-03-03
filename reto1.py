import pandas as pd
import json,csv
#Caso 1
def caso1():
   fichero=open("./Ficheros/reto.csv")
   print(fichero.read())
   fichero.close()

#Caso 2
def caso2():
   jsonData=toJson()
   print(jsonData)

#Caso 3
def caso3():
   #Ordeno el json por matricula
   jsonData=toJson()
   data_sort=sorted(jsonData,key=lambda x:x["Matricula"])
   totales=[]
   i=0
   distancia=0
   for vehiculo in data_sort:
      if i==0:
         #La primera vez la distancia la igualo a la del vehiculo actual
         distancia=vehiculo["Distance"]
      elif vehiculo["Matricula"] == data_sort[i-1]["Matricula"]:
         #Si las matriculas son iguales sumo la distancia
         distancia+=vehiculo["Distance"]
      else:
         #Matriculas distintas Añado el total de distancia a totales
         #Igualo distancia al vehiculo actual
         totales.append([data_sort[i-1]["Matricula"],distancia])
         distancia=vehiculo["Distance"]
      i+=1
   for datos in totales:
      print("El vehículo con matricula:",datos[0],"ha recorrido",datos[1],"metros")
#Caso5
def caso5():
   vehiculos_csv = pd.read_csv('./Ficheros/reto.csv')
   # Cambio el timestamp al formato de fecha
   vehiculos_csv['Pos_date'] = pd.to_datetime(vehiculos_csv["Pos_date"], unit="ms",utc=True)
   vehiculos_csv["Pos_date"]=vehiculos_csv["Pos_date"].dt.strftime('%d-%m-%Y %H:%M:%S')
   #Ordeno por el campo fecha
   vehiculos_ordenado = vehiculos_csv.sort_values('Pos_date',ascending=False)
   #Creo el nuevo fichero
   vehiculos_ordenado.to_csv('./Ficheros/ordenadoPorFecha.csv', index=False)

def toJson():
   csv_data = pd.read_csv("./Ficheros/reto.csv", sep=",")
   jsonData=csv_data.to_json(orient="records")
   data = json.loads(jsonData)
   return data

print("Que caso desea ejecutar")
num=input()
if num=="1":
   caso1()
elif num=="2":
   caso2()
elif num=="3":
   caso3()
elif num=="5":
   caso5()
else:
   print("El caso no ha sido resuelto")