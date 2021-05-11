#definir variables
print("Ejercicio 16")
#datos de entrada
salario= 950
puntosP=int(input("Ingrese sus puntos obtenidos:"))
if puntosP >=0 and puntosP <=100 :
  premio = salario
elif puntosP >= 101 and puntosP <=150 :
  premio = salario * 2 
elif puntosP >=151 :
  premio = salario * 3
print("El bono que le corresponde es:",premio)