#REGEXP
#Python3.7
#jr2r

import re

cadena = "Aprendiendo expresiones regulares en Python. Python es un lenguaje de sintaxis sencilla."

palabra = "Python"

if re.search(palabra, cadena) is not None:
    print("Texto Encontrado")
else:
    print("Texto no encontrado")

textoEnc = re.search(palabra, cadena)
print(textoEnc.start())
print(textoEnc.end())
print(textoEnc.span())
print(re.findall(palabra, cadena))
print(len(re.findall(palabra, cadena)))