"""
Ejercicio 2.22¶
Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y
después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
"""
frase = input("Introduce una frase : ")
vocal = input("Introduce una vocal : ")

if len(vocal) == 1 and vocal in "aeiouAEIOU" :
    frase_final = frase.replace(vocal,vocal.upper())
    print(f"Frase modificada : \n"
          f"{frase_final}")
else:
    print("Error inesperado")