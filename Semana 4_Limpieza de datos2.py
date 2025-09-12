from pathlib import Path
ROOT = Path(__file__).resolve().parent
TXT  = ROOT/"Archivos" /"mediciones_200_mixto.txt"
contenido=[]
with open(TXT,'r', encoding= 'utf-8') as f:
    for linea in f:
        s=linea.strip() 
        if not s or s.startswith('#'):
            continue
        if not s or s.startswith('!'):
            continue
        s=s.replace(',','.')
        try:
            contenido.append(float(s))
        except ValueError:
            pass
Vmayor=[]
Vmenor=[]
for i in contenido:
    if i>=5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(len(Vmayor))
print(len(Vmenor))
    
        