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

