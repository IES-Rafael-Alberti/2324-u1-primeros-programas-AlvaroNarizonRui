"""
Ejercicio 2.17¶
Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e
imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
"""
def imprimirNombre(nombre,veces):
    while veces > 0:
        print(f"{nombre}")
        veces -= 1
#Entrada
nombre = input("Escribe tu nombre de usuario : ")
veces = int(input("Escribe un número : "))
#Procesamiento y salida
imprimirNombre(nombre,veces)
