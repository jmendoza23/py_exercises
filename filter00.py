#Filter
#Python 3.7
#jr2r
#

#Pares e Impares
#
# def numeroPar(num):
#     if num % 2 == 0:
#         return True

listNum = [17, 27, 8, 12, 30, 50, 15, 83, 92]

#Filter para mostar solo los numeros que cumplan con la funcion numero par, filter toma dos argumentos funcion e iterable.
#print(list(filter(numeroPar, listNum)))
#lamda permite realizar la operacion y no tener uqe usar una funcion para esto.
print(list(filter(lambda numeropar: numeropar%2 == 0,  listNum)))






        