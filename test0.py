# num1 = int(input("Numero1: "))
# num2 = int(input("Numero2: "))

# def DevuelveMax(num1, num2):
#     if num1 < num2:
#         print(num2)
#     elif num2 < num1 :
#         print(num1)
#     else:
#         print ("Son Iguales")
# print("El numero mas alto es:")
# DevuelveMax(num1, num2)
# ###################################################################

# print("Sign-Up")

# usrName = input("Name: ")
# usrAdrs = input("Address: ")
# usrPhone = input("Phone: ")

# usrData = [usrName, usrAdrs, usrPhone]

# print(usrData)

####################################################################

# num1 = int(input("Num1: "))
# num2 = int(input("Num2: "))
# num3 = int(input("Num3: "))

# media = (num1 + num2 + num3) / 3
# print("Media Aritmetica: ", media)

####################################################################

# print("Becas 2020")

# distEsc = int(input("Distancia: "))
# numHerm = int(input("Numero de Hermanos: "))
# ingFam = int(input("Ingreso Familiar: "))

# if distEsc > 40 and numHerm > 2 and ingFam < 20000:
#     print("Candidato a beca.")
# else:
#     print("No es Candidato.")

####################################################################

# clasOpt = ["Fotografia", "Cloud", "Scripting", "Containers"]
# print("Clases Optativas")
# asignatura = input("Escriba clase: ")

# if asignatura in clasOpt:
#     print("Clase asignada")
# else:
#     print("Clase no disponible")

####################################################################

#for i in range (1, 101):
#   print(i, end=" ")

####################################################################

# minLen = 8
# usrPsswd = input("Create new password: ")

# if " " in usrPsswd:
#     print("No blank spaces are allowed")
# else:
#     if len(usrPsswd) >= minLen:
#         print("Password Created!!!")
#     else:
#         print("8 minimum characters")

######################################################################
# counter1 = 0
# counter2 = 0
# usrEmail = input("Enter Email:")

# for i in range(len(usrEmail)):
#     if usrEmail[i] == "@":
#         counter1 = counter1+1
#     if usrEmail[i] == ".":
#         counter2 = 1
# if counter2==1 or counter1!=1:
#     print("Wrong Email")
# else: 
#     print("Email Correct")

######################################################################

# usrInput = int(input("Enter a number: "))
# prvNumber = 0
# while usrInput > prvNumber:
#     prvNumber = usrInput
#     usrInput = int(input("Enter a number: "))
# print("Exiting script...")
    
######################################################################

# usrInput = int(input("Enter a number:"))
# sumTotal = 0
# while usrInput > 0:
#     sumTotal += usrInput
#     usrInput = int(input("Enter a number:"))
# print("Total: "+str(sumTotal))
# print("Exiting script....")

######################################################################

# def generaPares(limite):
#     num=1
#     while num < limite:
#         yield num*2
#         num = num+1
# devuelvePares = generaPares(10)
# print(next(devuelvePares))
# for i in devuelvePares:
#     print(i)
# for i in range(1, 10):
#     print(next(devuelvePares))

######################################################################

# def devuelve_ciudades(*ciudades):
#     for elemento in ciudades:
#         yield from elemento # Obtine el subElemento.
        # for subElemento in elemento: #recorrer el elemento e imprime el subelemento
        #     yield subElemento

# ciudades_devueltas = devuelve_ciudades("Madrid", "Barcelona","Malaga","Valencia" )#Iterador
# print(next(ciudades_devueltas))
# print(next(ciudades_devueltas))


######################################################################

# # def suma(num1, num2):
#     return num1+num2

# def resta(num1, num2):
#     return num1-num2

# def multiplicación(num1, num2):
#     return num1*num2

# def division(num1, num2):
#     try:
#         return num1/num2
#     except ZeroDivisionError:
#         print("No es posible dividir entre 0")
#         return "Operation not valid"
# while True: #Ciclo infinito, revisa que cada linea sea True.
#     try:
#         num1 = int(input("Number1: "))  
#         num2 = int(input("Number2: "))
#         break #El break ayuda a romper el ciclo, el bloque hasta aqui es true por eso pasa al siguiente bloque.
#     except ValueError:
#         print("Wrong value, try again!!")

# usrOpt = input("Introduce operacion a realizar(sum, resta, multiplicacion, division): ")

# if usrOpt == "suma":
#     print(suma(num1, num2))
# elif usrOpt == "resta":
#     print(resta(num1, num2))
# elif usrOpt == "multiplicacion":
#     print(multiplicación(num1, num2))
# elif usrOpt == "division":
#     print(division(num1, num2))
# else:
#     print("Opcion incorrecta.")

# print("bla bla bla")

##########################################################################

# def divide():
#     try:
#         op1=(float(input("Number1: ")))
#         op2=(float(input("Number2: ")))
#         print("Result is: " + str(op1/op2))
#     except ValueError:
#         print("Wrong Value")
#     except ZeroDivisionError:
#         print("Error, divided by 0")
#     #except por si mismo captura todas las excepciones, NO es una buena practica.
#     finally: #Buena practica, utilizar el finally para cerrar una sesion(ejemplo: BD).
#         print("###Completed###")

# divide()

##########################################################################

# def evalAge(edad):
#     if edad <= 0:
#         raise ValueError("No se permiten edad negativas")
#     if edad < 20:
#         return "young"
#     elif edad < 40:
#         return "Not so young"
#     elif edad < 65:
#         return "Mature"
#     elif edad < 100:
#         return "Take care"
# print(evalAge(0))

##########################################################################

# import math

# def evalRoot(num1):

#     if num1 < 0:
#         raise ValueError ("El numero no puede ser cero o negativo")
#         #Raise se usa para crear un tipo de excepcion puede o no utilizar
#         #los tipos de excepcion por default de python. Pero para usar uno propio
#         #se debe crear una clase con la excepcion.
#     else:
#         return math.sqrt(num1)
# x = (int(input("Introduce un numero: ")))
# try:
#     print(evalRoot(x))
# except ValueError as error1: #Llamar a la excepcion y asignarla a una variable
#     print(error1)

# print("blabla")

############################################################################

# from tkinter import *

# class Main():
#     def __init__(self):
#         self.main = Tk()

#         #INTEGER
#         #self.integer = 0
#         self.integer = IntVar(0)

#         #BUTTONS
#         Button(self.main,text='Quit',command=self.main.destroy).pack()
#         Button(self.main,text='+',command=self.plus_one).pack()
#         Button(self.main,text='-',command=self.take_one).pack()

#         #ENTRY
#         Entry(self.main,textvariable=self.integer,justify=CENTER,width=4).pack()

#         #MAINLOOP
#         mainloop()

#     def plus_one(self):
#         self.integer.set(self.integer.get()+1)
#         #self.entry0.delete(0,END)
#         #self.entry0.insert(0,self.integer)

#     def take_one(self):
#         self.integer.set(self.integer.get()-1)
#         #self.entry0.delete(0,END)
#         #self.entry0.insert(0,self.integer)

# Main()





















