"""
Ejercicio 2.26¶
Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas,
y muestre por pantalla cada uno de los productos en una línea distinta.
"""
def leerProductos() -> str:
    carro = input("Escribe los productos de tu cesta separados por comas : ")
    return carro
def crearCesta(carro) -> list:
    cesta_lista = carro.split(",")
    return cesta_lista
def mostrarCesta(cesta_lista):
    n = 1
    for i in cesta_lista:
        print(f"{n} : {i}")
        n += 1
#Entrada
carro = leerProductos()
#Procesamiento
lista_compra = crearCesta(carro)
#Salida
mostrarCesta(lista_compra)