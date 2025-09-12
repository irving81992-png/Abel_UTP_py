from pathlib import Path  # impor el path de la libreria pathlib
ROOT = Path(__file__).resolve().parent #ruta de mi archivo
TXT = ROOT /"Archivos"/"mediciones_basico.txt"
contenido=[]
with open(TXT,'r',encoding='"utf-8"') as f:  #lee el tecto TXT y usa codificacion utf-8 y lo convierte en f
    for linea in f:   #lee linea por linea
        s=linea.strip()  #borra las lineas en blanco 
        if not s or s.startswith("#"):  #si empieza con # los borra si no encuentro que continue
            continue  #saltar fila
        if not s or s.startswith("!"): #si empieza con ! los borra si no encuentro que continue
            continue  #saltar fila
        s=s.replace(",",".")
        try:
            contenido.append(float(s))  #que contienes numero con coma y punto 
        except ValueError:
            pass
ValorMayor=[]
ValorMenor=[]
for i in contenido:  #hago una condicion con for  el i lo convierte en contenido
    if  i >= 5:
        ValorMayor.append(i)
    else:
        ValorMenor.append(i)
print(len(ValorMayor))  #len para ser el conteo
print(len(ValorMenor))