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

def grado2(m2):
    return m2[0][0] * m2[1][1] - m2[0][1] * m2[1][0]

def grado3(m3):
    A1 = m3[0][0] * grado2(insertar(m3[1][1],m3[1][2],m3[2][1],m3[2][2]))
    A2 = m3[0][1] * grado2(insertar(m3[1][0],m3[1][2],m3[2][0],m3[2][2]))
    A3 = m3[0][0] * grado2(insertar(m3[1][0],m3[1][1],m3[2][0],m3[2][1]))
    return A1 - A2 + A3

def sarrus(m3):
    A1 = m3[0][0] * m3[1][1] * m3[2][2] + m3[1][0] * m3[2][1] * m3[0][2] + m3[2][0] * m3[1][2] * m3[0][1]
    A2 = m3[0][2] * m3[1][1] * m3[2][0] + m3[1][2] * m3[2][1] * m3[0][0] + m3[0][1] * m3[1][0] * m3[2][2]
    return A1 - A2

def dibujar(m3):
    print("La matriz es: ")
    for i in range(len(m3)):
        print (m3[i])

matriz = [[2,4,6],[3,0,3],[2,2,3]]
dibujar(matriz)
print("El determinante iterativo es: ",grado3(matriz))
print("El determinante de Sarrus es: ", sarrus(matriz))