#definir variables
print("Ejercicio 3")
#Datos de entrada
costoP= 0
regaloideal=0
#Proceso
dineroactual=int(input("Ponga el dinero actual que posee:"))
if dineroactual <= 10 :
  regaloideal = "Tarjeta"
elif dineroactual >=11 and dineroactual <=100 :
  regaloideal = "Chocolates"
elif dineroactual >= 101 and dineroactual <=250 :
  regaloideal = "Flores"
elif dineroactual >251 :
  regaloideal = "Anillo"
print("El regalo que le podrias dar es:",regaloideal, "'Vamos Campeón'")
