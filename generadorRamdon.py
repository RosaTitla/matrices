import random

lista1=[]

for r in range(5):
    j=random.randrange(1,10)
    lista1.append(j)
print(lista1)

temps = [[h for h in range (random.randrange(1,10))] for d in range (random.randrange(1,10))]

print(temps)
