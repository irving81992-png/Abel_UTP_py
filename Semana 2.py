#generar un correo electronico con el nombre y la fecha que le diga al ingeniero en jefe
#los valores medidos por el sensor y la fecha de medicion
#exit=para borrar todo el terminal

import random as rd #importar funciones -mundo aleatorio
import datetime as dt #importar funciones - fecha
NOMBRE ="Abel" #constante por convecion  -str
edad = 32  #int 
Fecha = dt.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
voltaje =rd.randint(0,1023) #float

activo = True  #bool
#f-string(formato para cadena de caracteres,letras)
print(f"Hola Ingeniero ,{NOMBRE}.Edad:{edad}" )
print(Fecha)
#para float {voltaje:.5f} el valor de f nos indica el numero despues de la coma
print(f"voltaje medido: {voltaje:.2f}, V / Activo:{activo}")
#str cambiar de numero a texto
print(f"Tipos->edad:{type(edad).__name__},voltaje:{type(voltaje).__name__}")
