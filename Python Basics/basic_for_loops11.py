#Ejercicio 1
Tamaño grande - Dada una lista, escribe una función que cambie todos los números positivos de la lista a “big”.
Ejemplo: biggie_size([-1, 3, 5, -5]) devuelve la misma lista, pero cuyos valores ahora son [-1, "big", "big", -5] 

lista = [-1,2,3,-4]
for x in range(len(lista)):
    if lista[x] > 0:
        lista[x] = "big"
print(lista)


#Ejercicio 2
Contar positivos - Dada una lista de números, crea una función para reemplazar el último valor con el número de valores positivos.  
(Ten en cuenta que el 0 no se considera un número positivo).
Ejemplo: count_positives([-1,1,1,1]) cambia la lista original a[-1,1,1,3] y la devuelve
Ejemplo: count_positives([1,6,-4,-2,-7,-2]) cambia la lista original a [1,6,-4,-2,-7,2] y la devuelve 

def count_positives(lista):
    score = 0
    for x in range (len(lista)):
        if lista[x] > 0:
            score = score + 1
    print(f"valor {score}")
    lista.pop()
    lista.append(score)
    return lista
lista = [1,6,-4,-2,-7,-2,2,3,4,2,3,4]
print(count_positives(lista))

#Ejercicio 3
Suma total - Crea una función que tome una lista y devuelva la suma de todos los valores en el arreglo.
    Ejemplo: sum_total([1,2,3,4]) debería devolver 10
    Ejemplo: sum_total([6,3,-2]) debería devolver 7 

def sum_total(lista):
    suma = 0 # se crea variable suma para almacenar la suma de valores en la lista
    for x in range(len(lista)): # for loop ayuda iterar en valores de lista
        suma = suma + lista[x] # variable suma almacena y suma valores de lista
    return suma # return especifica el valor dentro de variable suma para cuando se llame a funcion
lista = [1,2,3,4,2,3,444]
print(sum_total(lista))

#Ejercicio 4
Promedio - Crea una función que tome una lista y devuelva el promedio de todos los valores.
Ejemplo: average([1,2,3,4]) debería devolver 2.5 

def average(lista):
    suma = 0
    for x in range(len(lista)):
        suma = suma + lista[x]
    promedio = suma / len(lista)
    return promedio
lista = [1,2,3,4]
print(average(lista))

#Ejercicio 4
Longitud - Crea una función que tome una lista y 
devuelva la longitud de la lista.

    Ejemplo: length([37,2,1,-9]) debería devolver 4
    Ejemplo: length([]) debería devolver 0 

def length(lista):
	longitud_lista = 0 # valor que contara las iteraciones de x en for loop
	for x in lista:
		longitud_lista += 1
	print(longitud_lista)
lista = [1,2,3,4,5]
length(lista)


#Ejercicio 5
Mínimo - Crea una función que tome una lista de números y 
devuelva el valor mínimo en la lista. (Opcional) Si la lista está vacía, 
haz que la función devuelva False.

    Ejemplo: minimum([37,2,1,-9]) debería devolver -9
    (Opcional) Ejemplo: minimum([])  debería devolver False 

def minimum(lista):
    if len(lista) != 0:
        valor_minimo = lista[0] # almacenara valor minimo en for loop al ser reemplazado
        for x in lista:
            if x < valor_minimo:
                valor_minimo = x
        return valor_minimo
    else:
        return False
lista = [1,2,3,2]
print(minimum(lista))

#Ejercicio 5
Máximo - Crea una función que tome una lista y devuelva el valor máximo en el arreglo. 
(Opcional) Si la lista está vacía, haz que la función devuelva False.

    Ejemplo: maximum([37,2,1,-9]) debería devolver 37
    (Opcional) Ejemplo: minimum([])  debería devolver False 

def maximum(lista):
    if len(lista) != 0:
        valor_maximo = lista[0]  #valor inicial sera reemplazado por valor maximo en for loop
        for x in lista:
            if x > valor_maximo:
                valor_maximo = x
        return valor_maximo
    else:
        return False
lista = [1,2,3,4,4,5,5,55,-33]
print(maximum(lista))

#Ejercicio 6
Análisis final (opcional) - Crea una función que tome una lista y
devuelve un diccionario que tenga la sumTotal, promedio, mínimo, máximo y la longitud de la lista.

    Ejemplo: ultimate_analysis([37,2,1,-9]) debería devolver {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37,        'length': 4} 

**** pongo 2 formas distintas ya que me costaron horas y terminando una se me ocurrio la segunda..
1.
def ultimate_analysis(lista):
    suma = 0
    valor_minimo = lista[0]
    valor_maximo = lista[0]
    longitud = 0
    ult_analysis = {}
    for xSuma in range (len(lista)):
        suma = lista[xSuma] + suma
        ult_analysis['sumTotal'] = suma    
    for xAvg in lista:
        promedio = suma / len(lista)
        ult_analysis['average'] = promedio
    for x in lista:
        if x >= valor_maximo:
            valor_maximo = x
            ult_analysis['maximum'] = valor_maximo
    for y in lista:
        if y <= valor_minimo:
            valor_minimo = y
            ult_analysis['minimum'] = valor_minimo
    for yLen in lista:
        longitud += 1
        ult_analysis['length'] = len(lista)
    return ult_analysis

lista = [1,2,3,4,5]
print(ultimate_analysis(lista))
2.
def ultimate_analysis(lista):
    ult_analysis = {}
    ult_analysis['sumTotal'] = sum(lista)
    ult_analysis['average'] = sum(lista)/len(lista)
    ult_analysis['maximum'] = max(lista)
    ult_analysis['minimum'] = min(lista)
    ult_analysis['length'] = len(lista)
    return ult_analysis
lista = [12,12,14]

print(ultimate_analysis(lista))

#Ejercicio 7
Lista inversa (opcional) - Crea una función que tome una lista y devuelva esa lista con los valores invertidos.  
Haz esto sin crear una segunda lista. (Se sabe que este desafío aparece durante las entrevistas técnicas básicas).

    Ejemplo: reverse_list([37,2,1,-9]) debería devolver [-9,1,2,37]       
def reverse_list(lista):
	lista = lista[::-1] 
	return lista
lista = [37,2,1,-9,2,3,4]


print(reverse_list(lista))
