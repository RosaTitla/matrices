
#temps = [[h for h in range (3)] for d in range (2)]
#print(temps)

matrizA = []
fila=[]
for i in range(3):
    fila = []
    for j in range(3):
        num= int(input('numero'))
        fila.append(num)
    matrizA.append(fila)

#paso 3 mostrar la matriz
for f in matrizA:
    print(f)