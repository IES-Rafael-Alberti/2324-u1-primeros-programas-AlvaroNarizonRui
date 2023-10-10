"""
Ejercicio 2.5
Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
"""
def calcularIVA(importe_base,iva) -> float:
    iva_aplicado = importe_base*iva/100
    importe_final = iva_aplicado + importe_base
    return importe_final
#Entrada
importe_base = float(input("Escribe el importe sin IVA : "))
iva = int(input("Qué porcentaje de IVA se va a aplicar : "))
#Procesamiento
importe_final = calcularIVA(importe_base,iva)
#Salida
print(f"El importe total es : {importe_final} euros")
