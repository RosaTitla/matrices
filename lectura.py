lista1=[1,0]
lista2=[1,2]
matriz1=[lista1,lista2]
#matriz de 2 filas
matriz2=[[2,4],[7,1]]
#matriz de 3 filas
matriz3=[[1,2,3],[4,5,6],[7,8,9]]
print('matriz 1')
for fila in matriz1:
    print(fila)
print('matriz 2')
for fila in matriz2:
    print(fila)
print('matriz 3')
for fila in matriz3:
    print(fila)


matrizA=[[1,2],[3,4]]


for fila in matriz1:
    for i in fila:
       print(i,end='\t')
    print()

temps = [[h for h in range (2)] for d in range (2)]
#print(temps)
x,y=0
for fi in matriz1:
    print(fi[x][y])
    x+=1
    y+=1

