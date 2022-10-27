# 1. Actualizar valores en diccionarios y listas

# 1. Cambiar el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [[5,2,3], [15,8,9]].
# 2. Cambiar el last_name del primer alumno de 'Jordan' a 'Bryant'
# 3. En el sports_directory, cambie 'Messi' por 'Andrés'.
# 4. Cambiar el valor 20 en z a 30.

# x = [ [5,2,3], [10,8,9] ] 
# students = [{'first_name':  'Michael', 'last_name' : 'Jordan'},{'first_name' : 'John', 'last_name' : 'Rosales'}]
# sports_directory = {'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],'soccer' : ['Messi', 'Ronaldo', 'Rooney']}
# z = [ {'x': 10, 'y': 20} ]

# x[1][0] = 15 # para cambiar valor de una lista dentro de otra lista, se identifica la lista anidada y luego el valor a cambiar en esa lista

# students[0]["last_name"] = "Bryant" # para cambiar el valor en un diccionario se especifica la ubicacion y luego el key

# sports_directory["soccer"][0] = "Andrés"

# z[0]["y"] = 30

# print(x)
# print(students)
# print(sports_directory)
# print(z)



# 2. Iterar a través de una lista de diccionarios

# Crear una función iterateDictionary(some_list 
# para que, dada una lista de diccionarios, la función recorra cada diccionario de la lista 
# e imprima cada llave y el valor asociado. Por ejemplo, dada la siguiente lista:

 
# debería generar: (está bien si cada par llave-valor termina en 2 líneas separadas;
# ¡bonificación para que aparezcan exactamente como se muestra a continuación!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# a = students[0]
# a2 = ''
# a3 =''
# students[0]

# for x in a.items():
#     a2 = x[0]
#     for y in a.items():
#         y = x[0]
#     print(a2,y)

# d = ''
# def iterateDictionary(students):
#     for x in students:
#         for keys, values in x.items():
#             print(keys,values)
# iterateDictionary(students)


# 3. Obtener valores de una lista de diccionarios

# Crear una función iterateDictionary2(key_name, some_list) que, 
# dada una lista de diccionarios y un nombre de llave, imprima el valor almacenado en esa llave para cada diccionario. 
# Por ejemplo, iterateDictionary2('first_name', students) debería generar:
# students = [
#          {'first_name':  'Michael', 'last_name' : 'Jordan'},
#          {'first_name' : 'John', 'last_name' : 'Rosales'},
#          {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#          {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
# def iterateDictionary2(key_name, students):
#     if key_name == "first_name":
#         for x in students:
#             if key_name in (x):
#                 print(x[key_name])
        
#     elif key_name == "last_name":
#         for y in students:
#             if key_name in (y):
#                 print(y[key_name])
# iterateDictionary2("last_name",students)


# 4. Iterar a través de un diccionario con valores de lista

# Crear una función printInfo(some_dict) que, dado un diccionario cuyos valores son todos listas, 
# imprima el nombre de cada llave junto con el tamaño de su lista, 
# y luego imprima los valores asociados dentro de la lista de cada llave. Por ejemplo:
# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon


# dojo = {
#    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
#    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
# }
# def printInfo(dojo):
#     locations = list(dojo.values())[0]
#     print(len(locations), list(dojo)[0].upper())
#     for x in locations:
#         print(x)
#     print("\n")
#     instructors = list(dojo.values())[1]
#     print(len(instructors), list(dojo)[1].upper())
#     for y in instructors:
#         print(y)

# printInfo(dojo)