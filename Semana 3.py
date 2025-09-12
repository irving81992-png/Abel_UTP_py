import random as rd
lista=[] #lista vacia
for i in range(5): #inicio de un bucle es con el:
    num=rd.randint(1,10) #numeros aleatorios del 1 a 10
    lista.append(num) #append añade a la lista
print(lista)

vol_sqrt=[]
v=[4.5,2.32,4.88]
for i in v:
    vol_sqrt.append(i*i)
print(f"el voltaje al cuadrado es: {vol_sqrt}") #comando map

lecturas=[4.95,5.10,4.88]
for idx, vol in enumerate(lecturas,start=1):
    print(f"{idx}:{vol:.2f}V")
    
#primero crear un lista aleatoria
#verificar si lo valores son mayores o menores a 5v
#imprimir en cada caso voltaje alto o voltaje bajo

