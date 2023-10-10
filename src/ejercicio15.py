"""
Ejercicio 2.15¶
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se 
cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de 
dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros 
tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

Calcula el interés: capital * (1 + interes)
"""
def LeerDinero() -> float:
    entrada_dinero = float(input("Escribe la cantidad de ahorros depositados : "))
    return entrada_dinero
def calcularInteres(dinero) -> float:
    años_restantes = 3
    interes = 4
    importe_final = dinero - (dinero*interes/100)
    return importe_final
def salidaDinero(dinero1,dinero2,dinero3):
    print(f"La cantidad de dinero tras el primer año : {round(dinero_año1,2)} ")
    print(f"La cantidad de dinero tras el segundo año : {round(dinero_año2,2)}")
    print(f"La cantidad de dinero tras el año 3 : {round(dinero_año3,2)}")

#Entrada

entrada_ahorros = LeerDinero()

#Procesamiento

dinero_año1 = calcularInteres(entrada_ahorros)
dinero_año2 = calcularInteres(dinero_año1)
dinero_año3 = calcularInteres(dinero_año2)

#Salida

salida = salidaDinero(dinero_año1,dinero_año2,dinero_año3)