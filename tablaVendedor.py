
#creamos las listas
vendedor1=['Isaias', 21,33,55,66]
vendedor2=['Geremias', 20,33,50,66]
vendedor3=['Lucas', 30,30,12,60]
mat=[vendedor1,vendedor2,vendedor3]

print('VENTAS DEL MES DE MAYO')
n,s1,s2,s3,s4='Vendedor','Semana 1','Semana 2','Semana 3','Semana 4'
print('{:<12}{:>10}{:>10}{:>10}{:>10}'.format(n,s1,s2,s3,s4))
for vend in mat:
    print('{:<12}{:>8}{:>8}{:>10}{:>10}'.format(vend[0],vend[1],vend[2],vend[3],vend[4]))

ventasVendedor=[] #guarda la suma de cada vendedor suma filas
ventasPorSemana=[] #guarda la suma de cada semana suma columnas
sumPorVendedor=0

#sumar renglones
for ren in range(0,3):
    sumPorVendedor=0
    for col in range(1,5):
        sumPorVendedor+=mat[ren][col]
    ventasVendedor.append(sumPorVendedor)

listaB=[]
#sumar columnas
for col in range(1,5):
    sumPorSem=0
    for ren in range(0, 3):
        listaB.append=mat[ren][col]
    ventasPorSemana.append(sumPorSem)


#print('ventas por semana',ventasPorSemana)
#print('ventas por vendedor',ventasVendedor)

#insertamos en la pos 0 la cadena suma semanal
ventasPorSemana.insert(0,'suma Semanal')

#agregamos la lista ventasPorSemana a la matriz
mat.append(ventasPorSemana)


listaVendedores=[]


#deseo obtener el vendedor estrella (es el que vendio mas)
#creamos la matriz listaVendedores
for x in range(len(mat)-1):
    listaVendedores.append([mat[x][0],ventasVendedor[x]])

#print(listaVendedores)

print()

print('{:<12}{:>10}{:>10}{:>10}{:>10}'.format(n,s1,s2,s3,s4))
for vend in mat:
    print('{:<12}{:>8}{:>8}{:>10}{:>10}'.format(vend[0],vend[1],vend[2],vend[3],vend[4]))

print()
n,tot='Vendedor','ventas del mes'
print('{:<12}{:>10}'.format(n,tot))
for vend in listaVendedores:
    print('{:<12}{:>8}'.format(vend[0],vend[1]))

maxVentas=0
for i in ventasVendedor:
    if (i>maxVentas):
        maxVentas=i
        pos=ventasVendedor.index(i)
print()
print('vendedor estrella: {} ventas:${}'.format(listaVendedores[pos][0],listaVendedores[pos][1]))


let=chr(108)

let1=chr(105)
let2=chr(115)
let3=chr(116)
#print(let,let1,let2,let3)
#sum col
cont=0
for col in range(3):  #col=0
    sumPorSem=0
    for ren in range(3):   #ren=0
        if mat[ren][col]==mat[ren][col+1]:   #ren=0  col=1
            cont+=1
        if cont==3:
            print('determinante vale cero')
    ventasPorSemana.append(sumPorSem)


#sumar renglones
for ren in range(0,3):
    for col in range(1,5):
        if mat[ren][col]==0:
            cont += 1
if cont==16:
    print('matriz nula')

