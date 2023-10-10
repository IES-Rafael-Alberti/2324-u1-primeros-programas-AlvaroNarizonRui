"""
Ejercicio 2.27¶
Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla
una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de
unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
"""
def leerProducto() -> str:
    producto = input("Ingresa un producto : ")
    return producto
def leerUnidades() -> int:
    unidades = int(input("Qué cantidad : "))
    return unidades
def leerPrecio(producto) -> float:
    precio = float(input(f"Qué precio tiene el producto {producto} : "))
    return precio
def mostrarProducto(producto,unidades,precio):
    print("{producto}: {unidades:3d} unidades x {precio:9.2f}$ = {total:11.2f}$".format(producto = producto,unidades = unidades,precio = precio,total = unidades * precio))

#Entrada
producto = leerProducto()
unidades = leerUnidades()
precio = leerPrecio(producto)
#Procesamiento y salida
mostrarProducto(producto,unidades,precio)