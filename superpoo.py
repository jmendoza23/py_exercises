class persona():
    def __init__(self, nombre, edad, lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_residencia = lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad: ", self.edad, "\nResidencia: ", self.lugar_residencia)

class empleado(persona):
    def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #Se usa super para llamar a un metodo de la clase padre.
        self.salario = salario
        self.antiguedad = antiguedad
    def descripcion(self):
        super().descripcion() #Se usa super para llamar a la funcion descripcion de la clase padre persona.
        print("Salario: ", self.salario, "\nAntiguedad: ", self.antiguedad)
    

persona1 = persona("Antonio", 28, "Tenerife")
persona1.descripcion()
print(isinstance(persona1, empleado))