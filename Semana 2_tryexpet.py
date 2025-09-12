valor_txt=input("ingreso la temperatura en grados celcius:")

try:
    t=float(valor_txt)
    if  t>=30: 
        print("Alerta alta temperatura")
    elif t<0:
        print("Baja temperatura")
    else :
        print("Temperatura normal")

except ValueError:
    print("entrada invalidad ingrese eje.(26.5)")
