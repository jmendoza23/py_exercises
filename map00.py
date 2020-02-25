class employee:
    def __init__(self, nombre, cargo, salario):
      self.nombre = nombre
      self.cargo = cargo
      self.salario = salario

    def __str__(self):
        return "Name: {} | Position: {} | Salary: {}$".format(self.nombre, self.cargo, self.salario)

listEmployy = [
    employee("Joel", "IT", 1200),
    employee("Pedro", "IT", 2100),
    employee("Jazmiine", "IT", 2150),
    employee("Lili", "IT", 1800),
    employee("Tete", "IT", 21200)
]

def calc_employee(empleado):
    if (empleado.salario <= 1500):
        empleado.salario = empleado.salario*1.03
    return empleado

listaEmpleados = map(calc_employee, listEmployy)

for e in listaEmpleados:
    print(e)