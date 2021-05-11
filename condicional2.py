def ejercicio01():
  #definir variables
  print("Ejemplo Esctructura Condicional 01")
  montoP=0
  #datons de entrada
  cantidadx=int(input("Ingrese Cantidad de Lapices"))
  #proceso >condicional
  if cantidadx>=1000:
    montoP=cantidadx*0.80
  else:
    montoP=cantidadx*0.90
  #datos de salida
  print("El Monto a Pagar es", montoP)

ejercicio01() 
def ejercicio02():
  #defoinir variables
  print("Ejemplo estructura condicional 02")
  montoP=0
  #daton de entrada
  cantidadx=int(input("Ingrese Cantidad de personas")