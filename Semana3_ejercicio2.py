#primero crear un lista aleatoria
#verificar si lo valores son mayores o menores a 5v
#imprimir en cada caso voltaje alto o voltaje bajo

import random as rd
Vingreso=[]
for i in range (10):
    Vingreso.append(rd.randint(1,10))
print(Vingreso)
Vmayor=[]
Vmenor=[]
for i in Vingreso:
    if i>5:
        Vmayor.append(i)
    else:
        Vmenor.append(i)
print(Vmayor)
print(Vmenor)