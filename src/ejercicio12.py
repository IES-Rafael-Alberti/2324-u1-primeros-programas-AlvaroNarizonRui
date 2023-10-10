"""Ejercicio 2.12¶
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales."""
def calcularIMC(peso,estatura) -> float:
    imc = peso/estatura**2
    return imc
#Entrada
peso = float(input("Escribe tu peso en kg : "))
estatura = float(input("Escribe tu estatura en metros : "))
#Procesamiento
imc = calcularIMC(peso,estatura)
#Salida
print("Tu IMC es : ", round(imc,2))
