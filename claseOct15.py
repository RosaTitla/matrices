#Pasos para llenar una matriz
# con valores dados por el usuario
#paso 1 crear una matriz llena de ceros
matrizA = []
filaA = []
for i in range(3):
    filaA = [0 for i in range(3)]
    matrizA.append(filaA)

#paso 2 llenar la matriz con datos dados por el usuario
for i in range(3):
    for j in range(3):
        matrizA[i][j] = int(input('numero'))
#paso 3 mostrar la matriz
for f in matrizA:
    print(f)

