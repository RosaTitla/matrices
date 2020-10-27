
#Contar los números pares en la
#matrizA de 3 filas y 3 renglones
matrizA=[[10,24,35],[14,65,36],[27,18,49]]
matrizX=[[10,24,35],[10,24,35],[27,18,49]]
matrizZ=[[10,10,35],[14,14,36],[27,27,49]]
matrizB=[[10,24,35],[14,65,36],[27,18,49]]

matrizC=[[1,24,35],[14,65,36],[27,18,49]]
matrizD=[[10,24,35],[14,65,36],[27,18,49]]
for ren in range(3):
    for col in range(3):
        print(matrizX[ren][col],end='\t')
    print()

miMax=0
for ren in range(3):
    for col in range(3):
        if matrizA[ren][col]>miMax:
            miMax=matrizA[ren][col]
            posren=ren
            poscol=col
print('maxim',miMax, 'pos',posren,poscol)

miMin=10000
for ren in range(3):
    for col in range(3):
        if matrizA[ren][col]<miMin:
            miMin=matrizA[ren][col]
print('maxim',miMin)
cont=0
for ren in range(3):
    for col in range(3):
        if matrizC[ren][col]==matrizD[ren][col]:
           cont+=1
if cont==4:
    print('si es matriz diagonal')
print('maxim',miMax)


# numBuscar=input('num')
# listaA=[]
# cont=0
# for ren in range(3):
#     for col in range(3):
#         if matrizA[ren][col]==numBuscar:
#
#             listaA.append(matrizA[ren][col])
#             cont+=1
# print('total de pares',cont)