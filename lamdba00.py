# Funciones lambda (funciones anonimas), abreviar la sintaxis. Consiste en resumir una funcion en python por una funcion lambda. 
# Python 3.7
# Jr2r
#

#Funcion tradicional
'''def area_triangulo(base, altura):
    return (base*altura)/2

print(area_triangulo(5, 7))'''

#Funcion reducida con lambda, toma argumentos y despues de los dos puntos realiza la operacion.
#Las operaciones logicas o ciclos no son validos en lambda.
#Funciones rapidas(on the go, on demand, online) para utilizar por un momento.
area_triangulo = lambda base, altura:(base*altura)/2
alcubo = lambda numero:pow(numero, 3)

#Lambda con format.

destValor = lambda comision:"¡{}!$".format(comision)

comisionEmple=1890
print(destValor(comisionEmple))
