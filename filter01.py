class employee:
    def __init__(self, nombre, cargo, salario):
      self.nombre = nombre
      self.cargo = cargo
      self.salario = salario

    def __str__(self):
        return "Name: {} | Position: {} | Salary: {}$".format(self.nombre, self.cargo, self.salario)

listEmployy = [
    employee("Joel", "IT", 91202),
    employee("Pedro", "IT", 123210),
    employee("Jazmiine", "IT", 129232),
    employee("Lili", "IT", 92129),
    employee("Tete", "IT", 21202),
    employee("Sara", "IT", 11202),
    employee("Leo", "IT", 81202),
    employee("Ana", "IT", 41202),
    employee("Jose", "IT", 121202),
]

max_salaries = filter(lambda employ:employ.salario > 100000, listEmployy)

for e in max_salaries:
    print(e)