#definir variables
print("Ejercicio 4")
#Datos de entrada 
montoP=0
#proceso
cantidadX=int(input("Ingrese cantidad de horasde uso de estacionamiento:"))
if cantidadX >= 1 and cantidadX <= 2 :
  montoP= cantidadX * 5
elif cantidadX >= 3 and cantidadX <= 5 :
  montoP= cantidadX * 4
elif cantidadX >= 6 and cantidadX <= 10 :
  montoP= cantidadX * 3
elif cantidadX > 10  :
  montoP= cantidadX * 2
#datos de salida
print("El precio final es:",montoP)
