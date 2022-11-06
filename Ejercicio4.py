class polinomio(object):
    def __int__(self):
        self.gradomayor = None
        self.contenido = {}
    
    def agregrar(self, grado, valor):
        self.contenido[grado] = valor
        if self.gradomayor<grado:
            self.gradomayor = grado
    
    def obtener(self, grado):
        return self.contenido[grado]

    def restar(self, polinomio1, polinomio2):
        menor = polinomio1 if (polinomio1.grado < polinomio2.grado) else polinomio2
        mayor = polinomio2 if (menor < polinomio1) else polinomio1
        self.contenido = mayor.contenido
        for i in range(0, menor.grado + 1):
            try:
            
       
