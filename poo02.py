class vehiculos():
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False
    
    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True

    def estado(self):
        print("Marca: ", self.marca, "\nModelo: ", self.modelo, "\nEn Marcha: ", self.enmarcha,
             "\nAcelerando: ", self.acelera, "\nFrenando: ", self.frena)

class moto(vehiculos): #Herencia, se hereda el constructor(estado inicial) a la sub clase (moto).
    hcaballito=""

    def caballito(self): #Metodo propio de la clase moto
        self.hcaballito = "Haciendo caballito"

    def estado(self): #Metodo clase sobre escribe el valor inicial de estado, agregando funcion propia(hcaballito)
        vehiculos.estado(self)
        if(self.enmarcha):
            print(self.hcaballito)

class furgoneta(vehiculos):#Herencia, se hereda el constructor(estado inicial) a la sub clase (furgoneta).
    
    def carga(self, cargar):
        self.cargado=cargar
        if(self.cargado): #Por default este tipo de IF busca un valor TRUE
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta cargada"

#Herencia multiple es valida class ejemplo1(Metodo1, Metodo2...Metodon)el primer metodo es el que tiene preferencia
miMoto = moto("Honda", "XRZGH-87399")
#miMoto.arrancar()
#miMoto.caballito()
miMoto.estado()
mifurgoneta = furgoneta("FORD", "TCH3203G")
mifurgoneta.estado()
print(mifurgoneta.carga(False))
