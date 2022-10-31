def hanoi(n):
    if n == 1:
        contador = 1
    else:
        contador = (2*hanoi (n-1)+1)
    return contador

n = int(input("Introduzca el numero de discos de la torre hanói: "))
print("se necesitan {} movimientos para mover {} discos".format(hanoi(n),n))
