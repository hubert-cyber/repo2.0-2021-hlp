#Definicion de variables
print("Ejercicio 18")
#Datos de entrada
bono=0
sueldo= 1800
print("\t.:Opciones para el bono:.")
print("1. Digite esta opcion si Ud. tiene mas de 4 años de servicio")
print("2. Digite esta opcion si Ud. tiene menos o igual a 4 años de servicio")
print("3. Digite esta opcion si Ud. percibe un salario menor a 2000")
print("4. Digite esta opcion si Ud. percibe un ralario mayor a 2000")
opcion = int(input("Digite una opcion: "))
print()
if opcion==1:
  extra = float(input("Cuantos años de servicio tiene? → "))
  sueldobono=1800 * 0.25
  if extra >4:
    bono = sueldobono
  print("Su bono sera de:", bono)
elif opcion==2:
  extra = float(input("Cuantos años de servicio tiene? → "))
  if extra <= 4:
    sueldobono= 1800 * 0.20
    bono = sueldobono
  print("Su bono sera de:", bono)
elif opcion==3:
  extra = float(input("Cuanto de salario percibe? → "))
  if extra < 2000:
    bono= extra * 0.25
  print("Su bono sera de:",bono)
elif opcion==3:
  extra = float(input("Cual es su salario que percibe? → "))
  if extra >=2000:
    bono= extra * 0.20
  print("Su bono sera de:",bono)

