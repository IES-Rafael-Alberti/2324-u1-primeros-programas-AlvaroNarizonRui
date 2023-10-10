"""
Ejercicio 2.19¶
Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca
muestre por pantalla "NOMBRE tiene n letras.", donde NOMBRE es el nombre de usuario en mayúsculas y n es el número
de letras que tienen el nombre.
"""
nombre = input("Escribe tu nombre : ")
numero_letras = len(nombre)
print(f"El nombre {nombre} tiene {numero_letras} letras")