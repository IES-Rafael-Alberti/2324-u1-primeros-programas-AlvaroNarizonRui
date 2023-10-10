"""
Ejercicio 2.6
Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y 
el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).
"""
def calcularImporteBase(importe_final) -> float:
    iva = importe_final*10/100
    importe_base = importe_final - iva
    return importe_base
#Entrada
importe_final = float(input("Escribe el importe final de un artículo : "))
#procesamiento
importe_base = calcularImporteBase(importe_final)
#Salida
print(f"El importe sin IVA de tu artículo son  {importe_base} euros")