#define datos de entrada
print("Ejercicio 17")
#datos de entrada
paqueteA="A: 1 televisor, 1 modular, 3 pares de zapatos, 5 camisas y 5 pantalones"
paqueteB="B: 1grabadora, 3 pares de zapatos, 5 camisas y 5 pantalones"
paqueteC="C: 2 pares de zapatos, 3 camisas y 3 pantalones"
paqueteD="D: 1 par de zapatos, 2 pares de camisas y 3 pares de pantalones"
Trecibido= int(input("Ya llego diciembre, coloque Ud. el monto recibido:"))
if Trecibido >= 50000 :
  podracomprar = paqueteA
elif Trecibido <50000 and Trecibido >= 20000 :
  podracomprar = paqueteB
elif Trecibido <20000 and Trecibido >= 10000 :
  podracomprar = paqueteC
elif Trecibido <10000 :
  podracomprar = paqueteD
print("Ud. podra comprar el paquete", podracomprar)