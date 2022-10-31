def matriz1(filas,columnas):
    matriz = [None] * filas
    for i in range(filas):
        matriz[i] = [None] * columnas
    return matriz

def insertar(a,b,c,d):
    matriz = matriz1(2,2)
    matriz[0] [0] = a
    matriz [0] [1] = b
    matriz[1] [0] = c
    matriz [1] [1] = d
    return matriz