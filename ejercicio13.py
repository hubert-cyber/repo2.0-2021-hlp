#definir variables
print("Ejercicio 13")
#datos de entrada
costo=0
cantidadealumnos=int(input("Ponga el numero de alumnos para calcular costo:"))
if cantidadealumnos >= 100: 
  costo= cantidadealumnos * 20 
elif cantidadealumnos >= 50  and cantidadealumnos <100:  
  costo = cantidadealumnos * 35
elif cantidadealumnos >=20 and cantidadealumnos <=49: 
  costo = cantidadealumnos * 40
elif cantidadealumnos < 20:
  costo = cantidadealumnos * 70
print("El pasaje total es:", costo)