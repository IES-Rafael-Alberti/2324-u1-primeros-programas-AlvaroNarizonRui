"""
Ejercicio 2.20¶
Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código
del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte
por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
"""
numero_telefono = input("Escribe un número de teléfono con el siguiente formato (+34-XXXXXXXXX-XX) : ")
print(len(numero_telefono))

if(numero_telefono[:4] == "+34-" and len(numero_telefono) == 16):
    numero_dividido = numero_telefono.split("-")
    print(f"El número de teléfono sin el prefijo y sin la extensión es : {numero_dividido[1]}")
else:
    print("El número introducido no cumple con el formato")
