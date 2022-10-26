# Cuenta regresiva - Crea una función que acepte un número como entrada. 
# Devuelve una lista nueva que cuenta de uno en uno, desde el número (como elemento 0) hasta 0 (como último elemento).
# Ejemplo: cuentaregresiva(5) debe devolver la lista: [5,4,3,2,1,0] 
def cuenta_regresiva(numero): # se pasa el parametro numero el cual, al momento de llamar la funcion completara el codigo segun el numero dado
    lista = []
    while numero >= 0: # mientras numero dado sea mayor a 0
        lista.append(numero) # se agregara el numero dado al llamar la funcion a la lista
        numero = numero -1 # despues de agregar el numero se descuenta 1 para seguir con el bloque de codigo
    print(lista)
cuenta_regresiva(133) 


# Print y return -  Crea una función que reciba una lista con dos números. Imprime el primer valor y devuelve el segundo.
#     Ejemplo: : print_and_return([1,2]) debe imprimir 1 y devolver 2 
# def print_and_return(lista):
#     print(f"print( {lista[0]})") # diferenciador personal, opte por el para validar print vs return
#     r = lista[1]
#     return r
# lista = [3,10]
# print(print_and_return(lista))


# Primero más longitud - Crea una función que acepte una lista y devuelva la suma del primer valor de la lista, más la longitud de la lista.
# Ejemplo: first_plus_length([1,2,3,4,5])  debe devolver 6 (primer valor): 1 +length: 5) 

# def first_plus_length(lista):
#     suma = lista[0] + len(lista)
#     print(f"primer valor de lista {lista[0]}")
#     print(f"longitud de lista {len(lista)}")
#     print(f" suma {suma}")
#     return suma
# lista = [1,3]
# print(first_plus_length(lista))


# Esta longitud, ese valor - Escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, y cuyos valores sean, todos, el valor dado.
#     Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
#     Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2] 

# def length_and_value(a,b):
#     lista = []
#     while a > 0:
#         lista.append(b)
#         a = a - 1
#     return lista
# print(length_and_value(33,3))

# def lav(a,b):
#     lista2 = []
#     for x in range(a):
#         lista2.append(b)
#     return lista2
# print(lav(33,3))


# Valores mayores que el segundo (opcional)
# Escribe una función que acepte una lista y cree una nueva que contenga solo los valores de la lista original que sean mayores que su segundo valor. 
# Imprime cuántos valores son y luego devuelve la lista nueva. Si la lista tiene menos de 2 elementos, has que la función devuelva False
#  Ejemplo: values_greater_than_second([5,2,3,2,1,4]) debe imprimir 3 y devolver [5,3,4]
#  Ejemplo: values_greater_than_second([3]) debe devolver False



def values_greater_than_second(lista):
    lista_final = []
    if len(lista) < 2: # si la lista tiene menos de 2 elementos devuelve False
        return False
    else:
        segundo_valor = lista[1] # se declara variable segundo valor
        for x in range(len(lista)):
            if max(lista) > segundo_valor: # si el mayor mas alto de la lista es mayor a segundo valor
                lista_final.append(max(lista)) # sera agregado a una nueva lista
                lista.remove(max(lista))# se elimina el valor maximo para seguir con el segundo mas alto
        print(f"longitud de nueva lista: {len(lista_final)}")
    return lista_final
lista = [5,2,3,2,1,4]
print(values_greater_than_second(lista))


# # fueron hooooras y horas ... pero resulto


