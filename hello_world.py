
#generar un correo electronico con el nombre y la fecha que le diga al ingeniero en jefe
#los valores medidos por el sensor y la fecha de medicion
import random as rd #importar funciones -mundo aleatorio
import datetime as dt #importar funciones - fecha
nombre ="Abel"
edad = 32
Fecha = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
v = rd.randint(0,1023)

print("Hola Ingeniero " + nombre)
print(Fecha)
print("volataje medido " + str(v))
#str cambiar de numero a texto

