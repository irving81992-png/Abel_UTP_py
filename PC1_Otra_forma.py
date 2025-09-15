import csv
from datetime import datetime
from pathlib import Path
ROOT=Path(__file__).resolve().parent
TXT= ROOT/"Archivos"
IN_FILE=TXT/"voltajes_250_sucio.csv"  #archivos de ingreso
OUT_FILE=TXT/"voltajes_250_limpio.csv" #archivos de salida
#apertura de archivos
with open(IN_FILE,'r',encoding='utf-8',newline="")as fin,\
     open(OUT_FILE,'w',encoding='utf-8',newline="")as fout:
     leer= csv.DictReader(fin,delimiter=';')  #leer csv
     escribir=csv.DictWriter(fout,fieldnames=["timestamp","value"])  #escribir csv crea archivo y cabecera
     escribir.writeheader()
     #leer linea por lineal y selecionar en crudo=raw
     total=kept=0 #creo para aumentar la linea y aumentarse
     for  row in leer:
        total +=1
        ts_raw  = (row.get("timestamp") or "").strip()  #utilizo row.get para hallar cada unas de las linea tiemstamp y strip para eliminar vacios
        val_raw = (row.get("value") or "").strip() #utilizo row.get para hallar cada unas de las linea value y strip para eliminar vacios
   #Limpieza de datos       
        val_raw=val_raw.replace(',','.') #(",",".")
        val_low=val_raw.lower()  #comando lower cambio de 
        if not val_low or val_low.startswith('NA'):
            continue
        try:
            val=float(val_raw)
        except ValueError:
            continue
   #Limpieza de datos de tiempo
        ts_clean=None
        for fmt in ("%Y-%m-%dT%H:%M:%S","%d/%m/%Y %H:%M:%S"):
            try:
                dt=datetime.strptime(ts_raw,fmt)
                ts_clean=dt.strftime("%Y-%m-%dT:%M:%S")
                break
            except ValueError:
                pass
    #grabar datos en escribir  
        escribir.writerow({"timestamp":ts_clean,"value":f"{val:.3f}"})
        kept += 1