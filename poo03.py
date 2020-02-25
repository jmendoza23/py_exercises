class Coche():

    def desplazamiento(self):
        print("Me muevo en 4 ruedas")
class Moto():   
    def desplazamiento(self):
        print("Me muevo en 2 ruedas")
class Camion():
    def desplazamiento(self):
        print("Me muevo en 6 ruedas")
def desplazamientovehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Coche()
desplazamientovehiculo(miVehiculo)