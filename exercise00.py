from functools import reduce

towns = [{
         'name': 'Manchester',
         'population': 58241
         }, 
         {'name': 'Coventry', 
         'population': 12435
         }, 
         {'name': 'South Windsor',
          'population': 25709
          }]


# Mi intento         
# cityList = []
# for town in range(len(towns)):
#     city = towns[town]['name']
#     cityList.append(city)
# print(cityList)

#Lista comprensiva, usa la funcion get para obtener el valor dentro de la llave.
#town_names = [town.get('name') for town in towns]

# Lista crada con map y funcion lambda que obtiene el valor dentro de la llave, se pasa como segundo argumento
# el objeto iterador.
#town_names = list(map(lambda town: town.get('name'), towns))
#print(town_names)

#Listas anidadas, se obtiene el elemento buscando en la llave de un diccionario
# town_names = [town.get('name') for town in towns]
# town_population = [town.get('population') for town in towns]
#print(list(zip(town_names, town_population)))
#Se crean dos listas con zip, los elementos de estas listas se crean con un listas anidadas, las llaves y valores del diccionario se acceden mediante la funcion get y el nombre de llave.
#town_names, town_populations = zip(*[(town.get('name'), town.get('population')) for town in towns])
#print(town_names, town_population)

#Crear un diccionario por iteraciones.
# namesPopuDic = {}
#for town in range(len(town_names)):
#    namesPopuDic[town_names[town]] = town_populations[town]

#Lista anidada de diccionarios, se crea la estructura de llaves y valores del diccionario.
#mydic2 = [{'name': town_names[town],
#          'population': town_populations[town]}
#           for town in range(len(town_names))]

totalP = 0
for p in towns:
    totalP += p.get('population')

print(totalP)

total_population = sum(town.get('population') for town in towns)
print(total_population)

total_popu = reduce(lambda total, town: total + town.get('population'), towns, 0)
print(total_popu)

