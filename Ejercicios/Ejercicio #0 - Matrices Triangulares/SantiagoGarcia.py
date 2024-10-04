dimension=int(input())
def carga_matriz(tamaño):
    matriz = [[0 for c in range(tamaño)]for f in range(tamaño)]
    for filas in range(tamaño):
        palabra = input()
        if palabra[-1] == " ": palabra = palabra[0:len(palabra)-1]
        numero,col = "",0
        for i in range(len(palabra)):
            if palabra[i] != " ": numero+=palabra[i]
            else:
                matriz[filas][col] = int(numero)
                col+=1
                numero = ""
        matriz[filas][col] = int(numero)
    return matriz
matriz=carga_matriz(dimension)
bandera=0
for z in matriz: print(z)
if matriz[dimension-1][0]==0:
    for i in range(dimension):
        for j in range(dimension):
            if j<i and matriz[i][j]!=0:
                bandera=1
    if bandera==0: print("Si")
elif matriz[0][dimension-1]==0:
    for i in range(dimension):
        for j in range(dimension):
            if j>i and matriz[i][j]!=0:
                bandera=1
    if bandera==0: print("Si")
else: 
    print("No")
