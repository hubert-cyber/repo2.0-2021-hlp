#definir variables
print("Ejercicio 14")
#Datos de entrada
costoP= 0
regaloideal=0
#Proceso
nota=int(input("Ponga la nota actual que posee:"))
if nota >= 10:
  calificacion="A"
elif nota >= 9:
  calificacion="B"
elif nota >= 8:
  calificacion="C"
elif nota >=6 and nota <=7:
  calificacion="D"
elif nota <=5 and nota >=0:
  calificacion="F"
print("Su calificacion final es:", calificacion)