print("1. Comprobar si una matriz de orden 3, es simétrica.")
matriz1 = [[6,3,1],
           [3,2,0],
           [1,9,0]]
result = "V";
for x in range(0,3):
    for y in range(0,3):

        if (matriz1[x][y] != matriz1[y][x]):
            result = "F"
            x=3
            break
if result == "V":
    print("La matriz es simetrica")
else:
    print("La matriz no es simetrica")