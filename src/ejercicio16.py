"""
Ejercicio 2.16¶
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa
debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento 
que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
"""
PRECIO_PAN = 3.49
def leerPan() -> int:
    lectura = int(input("Escribe el número de barras vendidas : "))
    return lectura
def calcularPan(numerobarras) -> float:
    calculo_barras = numerobarras * (PRECIO_PAN*60/100)
    return calculo_barras
def salidaPan(cantidad,descuento):
    print(f"Una barra de pan cuesta : {PRECIO_PAN} \n El descuento por no ser fresca es del 60% \n El coste final por {cantidad} es {round(descuento,2)} euros")

#Entrada
entrada_pan = leerPan()

#Procesamiento
descuento_pan = calcularPan(entrada_pan)

#Salida
salida_pan = salidaPan(entrada_pan,descuento_pan)

