"""
Ejercicio 2.13¶
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla los siguienteS: "la división de n entre m da un cociente c y un resto r",
donde n y m son los números introducidos por el usuario, y c y r son el cociente y el resto de la división entera respectivamente.
"""
def division(numero1,numero2) -> int:
    cociente = int(numero1 / numero2)
    return cociente
def calcularResto(numero1,numero2) -> int:
    resto = int(numero1 % numero2)
    return resto
#Entrada
numero1 = int(input("Escribe un número : "))
numero2 = int(input("Escribe otro número : "))
#Procesamiento
cociente = division(numero1,numero2)
resto = calcularResto(numero1,numero2)
#Salida
print (f"la división de {numero1} entre {numero2} da un cociente {cociente} y un resto {resto}")