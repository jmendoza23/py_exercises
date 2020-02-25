import re

lista_nombres = ["http//test.com", 
                 "http//test.org",
                 "http//test.net",
                 "http//test.co"]

for nombre in lista_nombres:
    if re.findall('[g]', nombre):
        print(nombre)