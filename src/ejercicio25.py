"""
Ejercicio 2.25¶
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla,
el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan
con un solo carácter.
"""

def leerFecha() -> str :
    fecha = input("Escribe una fecha con el formato dd/mm/aaaa : ")
    return fecha
def separar_fecha(fecha:str):
    dia = fecha[:fecha.find("/")]
    mes_año = fecha[fecha.find("/")+1:]
    mes = mes_año[:mes_año.find("/")]
    año = mes_año[mes_año.find("/")+1:]
    print(f"Dia : {dia} \n"
        f"Mes : {mes} \n"
        f"Año : {año}")
#lectura
fecha = leerFecha()

#procesamiento y salida
separar_fecha(fecha)
