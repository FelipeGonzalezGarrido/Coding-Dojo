# Ordenamiento con ALGORITMOS
# posible pregunta tecnica, escribir desde 0 algoritmo en 30min a 1 hora


#Intercambio de variables en python

# array = [1,5,3,3]

# array[0], array[1] = array[1], array[0] 
# mediante el indice de una lista, se puede seleccionar los valores a cambiar
# en este caso el primer y segundo valor


#Ordenamiento BubbleSort

# [1,5,3,3] Se trata de comparar el primer valor con el segundo.
# [1,5,3,3] Si el segundo valor es mayor al primero, se intercambian sus posiciones
# [1,5,3,3] Si el segundo valor es menor, entonces se comparara el segundo valor con el tercero.
# [1,3,5,3] Si el segundo valor es mayor al tercero, se intercambian de posicion y continua la comparacion
# [1,3,5,3] 
# [1,3,3,5]

# arr = [1,5,3,3] 
# def bubbleSort(arr): # funcion con lista como parametro
#     for j in range(len(arr)-1): # loop for con rango de lista para iterar a traves de lista.
#         for x in range(len(arr)-1-j): # 
#             print("\n","*"*30, "\ncomparing ", arr[x], arr[x+1]) # x arr[x] y arr[x+1], toma el valor del primer y segundo valor y los compara
#             print("array: ",arr)
#             if arr[x] > arr[x+1]: # si valor con indice x es mayor al valor siguiente con indice x+1 se realiza el cambio
#                 arr[x],arr[x+1]= arr[x+1], arr[x]
#                 print("Swapped", arr[x],arr[x+1])
#                 print("array is now: ",arr)
#             else: # si el valor de arr[x] no es mayor, no sera necesario intercambiar valores
# print(bubbleSort(arr))


#Ordenamiento por seleccion

# [11,6,4,2,7] El primer paso es buscar el valor minimo de una lista y moverlo al inicio. reemplazando su lugar con el valor inicial
# [2,6,4,11,7] Considerando el primer valor ordenado, se procede con el siguiente minimo sin incluir el primero
# [2,4,6,11,7] Con esto, y sin contar los valores que ya estan ordenados, se busca el tercer valor minimo
# [2,4,6,7,11] Siguiendo esta logica y segun tamanio de lista, se buscara el siguiente valor minimo


# def selectionSort(mi_lista):
#     for i in range(len(mi_lista) -1):
#         posicion_minimo = i # representa el valor comparativo inicial del algoritmo
#         j = i + 1 # valor ascendente por cada iteracion, representa el index de la lista a analizar
#         while j < len(mi_lista): # mientras j sea menor a cantidad de valores en lista
#             if mi_lista[posicion_minimo] > mi_lista[j]: # si mi_lista[indice valor minimo] es mayor a mi_lista[valor ascendente], inicialmente ambos seran 0
#                 posicion_minimo = j # si el if es verdadero, la variable "j" toma el valor minimo *procesado*
#             j += 1 # si el if es falso, el valor ascendente suma 1, lo que permite realizar la comparacion con el siguiente valor en la lista.
#         mi_lista[i], mi_lista[posicion_minimo] = mi_lista[posicion_minimo],mi_lista[i]
#     return mi_lista # este return permite identificar el valor minimo en la lista.
# mi_lista = [15,13,11,22,8]
# print(mi_lista)
# print(selectionSort(mi_lista))


#Ordenamiento por insercion

# Se recorren los elementos de una lista, comparando con el elemento anterior
#[7,3,1,2,4,6] este ordenamiento compara un elemento con el ubicado a la izquierda, por ende se parte desde indice 1 en lugar de 0.
#[7,3,1,2,4,6] si lista[n] > lista[-n] 


def porInsercion(lista):
    for x in range(1,len(lista)): # el ordenamiento por insercion compara un elemento con el ubicado a la izquierda. por ende se parte desde indice 1 en lugar de 0. (0 no tiene elementos a la izquierda)
        valor_inicial = lista[x] # lista = [3,2,1]  valor inicial = [2]
        i = x - 1  # i vale
        while i >= 0:
            if valor_inicial < lista[i]:
                lista[i+1] = lista[i] # camia el numero del espacio i al espacio de la derecha i +1
                lista[i] = valor_inicial # cambia valor al espacio i
                i = i - 1
            else:
                break




lista = [3,2,1]


porInsercion(lista)
print(lista)