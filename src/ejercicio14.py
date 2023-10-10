"""
Ejercicio 2.14¶
Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. 
Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben 
calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g 
y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule 
el peso total del paquete que será enviado.
"""
<<<<<<< HEAD
def LeerPayasos() -> int:
    payasos = int(input("Escribe el número de payasos : "))
    return payasos
def LeerMuñecas() -> int:
    muñecas = int(input("Escribe el número de muñeecas : "))
    return muñecas
=======
>>>>>>> 0190e00 (todos los ejercicios y sus respectivos tests (en los que veo que se pueden hacer tests))
def CalcularPedido(payasos,muñecas):
    peso_payasos = payasos*112
    peso_muñecas = muñecas*75
    print(f"Peso total del paquete : {peso_payasos+peso_muñecas} gramos")

#Entrada
<<<<<<< HEAD

entrada_payasos = LeerPayasos()
entrada_muñecas = LeerMuñecas()

#Funcionamiento y salida

CalcularPedido(entrada_payasos,entrada_muñecas)
=======
payasos = int(input("Escribe el número de payasos : "))
muñecas = int(input("Escribe el número de muñeecas : "))

#Funcionamiento y salida
CalcularPedido(payasos,muñecas)
>>>>>>> 0190e00 (todos los ejercicios y sus respectivos tests (en los que veo que se pueden hacer tests))
