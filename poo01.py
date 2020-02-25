class Coche(): #Definir clase, atributos y metodos
    def __init__(self): #Estado Inicial para los atributos, constructor.
        self.largoChasis = 250 # Valores iniciales para los atributos
        self.anchoChasis = 120
        self.__ruedas = 4 #Encapsulamiento de un atributo
        self.enMarcha = False

    def arrancar(self, arrancamos): #Esto es un metodo, primer argumento self para ser parte de la clase  y llamarse asi mismo.
        self.enMarcha = arrancamos
        if (self.enMarcha):
            chequeo=self.__chequeoint()

        if (self.enMarcha and chequeo):
            return "El coche esta en marcha"
        elif (self.enMarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no se puede arrancar el coche"
        else:
            return "El coche esta parado"

    def estado(self): #2do metodo y verifica el valor del atributo enMarcha
        print("Ancho del chasis: ", self.anchoChasis, "Largo chasis: ", self.largoChasis, "Num Llantas: ", self.__ruedas)
    
    def __chequeoint(self): # Metodo encapsulado.
        print("Inciando Chequeo...")
        self.gasolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"
        if (self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
            return True
        else:
            return False

miCoche = Coche() #Objeto de la clase o instancia
print(miCoche.arrancar(True)) #Cuando la funcion regresa un return, se tiene que imprimir la funcion
miCoche.estado() #Cuando la funcion regresa un print no es necesario usar el print fuera de la funcion
print("###############Segundo objeto###############")
miCoche2 = Coche() #Objeto de la clase o instancia
print(miCoche2.arrancar(False)) #Cuando la funcion regresa un return, se tiene que imprimir la funcion
miCoche2.estado() #Cuando la funcion regresa un print no es necesario usar el print fuera de la funcion
