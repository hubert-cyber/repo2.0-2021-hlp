#definir variables
print("Ejercicio 6")
costoP=0
descuentoP=0
#Datos de entrada
precioX=int(input("Ingrese el precio del producto:"))
if precioX >= 200.00 :
 descuentoP= precioX * 0.15
 costoP= precioX - descuentoP 
elif precioX >=100.00 and precioX <200.00 :
 descuentoP= precioX * 0.12
 costoP= precioX - descuentoP
elif precioX <100.00 :
 descuentoP= precioX * 0.10
 costoP= precioX - descuentoP  
print("El costo final es:$",costoP, "pesos", "con uso de descuento:$",descuentoP, "pesos")