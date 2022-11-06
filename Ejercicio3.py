class nave():
    def __init__(self, nombre, largo, tripulacion, pasajero):
        self.nombre = nombre
        self.largo = largo
        self.tripulacion = tripulacion
        self.pasajero = pasajero
    
    def __str__(self):
        return "{}: {} , {}, {}".format(self.nombre, self.largo, self.tripulacion, self.pasajero)

def imprimir(lista):
    print("nombre, largo, tripulacion, pasajero")
    for i in lista: 
        print(i)

def imprimir2(lista, nombre):
    for i in lista:
        if i.nombre == nombre:
            print(i)
def imprimir3(lista, longitud):
    for i in range(longitud):
        print(lista[i])

def imprimir4(lista,n):
    for i in lista:
        if i.pasajero >= n:
            print(i)
def imprimir5(lista,n):
    contador = 0
    for i in lista:
        if i.nombre[0] == n[0] and i.nombre[1] ==n[1]:
            print(i)
            contador += 1
    if contador == 0:
        print("no hay naves que empiecen por esa letra")


lista = []
a = nave("Halcon Milenario", 100, 500, 350)
lista.append(a)
b = nave("Estrella de la muerte", 300, 1000, 871)
lista.append(b)
c = nave("Ala-X", 80,100, 50)
lista.append(c)
d = nave("Caza TIE", 90, 150, 100)
lista.append(d)
e = nave("Destructor Estelar", 300, 1200, 1000)
lista.append(e)
f = nave("Lanzadera imperial", 200, 200,200)
lista.append(f)
g = nave("Supremacy", 300, 280, 250)
lista.append(g)
h = nave("Nave de Control de Droides clase Lucrehulk", 290, 490, 460)
lista.append(h)

nn= sorted(lista, key = lambda x:x.nombre)
imprimir(nn)
an= sorted(lista, key = lambda x:x.largo, reverse = True)
imprimir(an)
imprimir2(lista,"Halcon Milenario")
imprimir2(lista, "Estrella de la muerte")
ad = sorted(lista, key = lambda x:x.pasajero, reverse = True)
imprimir3(ad,5)
af = sorted(lista, key = lambda x:x.tripulacion, reverse = True)
imprimir3(ad,1)
imprimir3(lista,6)

print(an[0])
print(an[-1])
imprimir5(lista, "AT")


