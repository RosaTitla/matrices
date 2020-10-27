tablero  = []
print("matriz inicial")
# for i in range(4):
#     fila = [0 for j in range(4)]
#     tablero.append(fila)
#     print(fila)

tablero=[[0 for i in range(4)] for j in range(4)]

for row in tablero:
    print(row)


print("matriz diagonal")
for i in range(4):
    for j in range(4):
        if i==j:
            tablero[i][j]=1


for row in tablero:
    print(row)



#temps = [[0.0 for h in range (24)] for d in range (31)]
#print(temps)

