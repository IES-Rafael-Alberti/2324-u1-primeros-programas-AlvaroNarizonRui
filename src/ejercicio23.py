"""
Ejercicio 2.23¶
Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro
correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.
"""
correo = input("Escribe tu correo electronico : ")
while "@" not in correo:
    correo = input("Error, se te ha olvidado poner la '@' en el correo, vuelva a intentarlo : ")
correo_dividido = correo.split("@")
correo_nuevo = correo_dividido[0] + "@ceu.es"
print(f"Tu nuevo correo de la empresa es: \n"
      f"{correo_nuevo}")
