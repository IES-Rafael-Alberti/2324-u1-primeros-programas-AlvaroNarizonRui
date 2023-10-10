"""
Ejercicio 2.4¶
Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.
"""
def conversorFahrenheit(temperatura_celsius) -> float:
    fahrenheit = (temperatura_celsius*9/5)+32
    return fahrenheit
#Entrada
temperatura_celsius = float(input("Escribe una temperatura en grados celsius : "))
#Procesamiento
fahrenheit = conversorFahrenheit(temperatura_celsius)
#Salida
print(f"{temperatura_celsius}º son {fahrenheit}Fº")
