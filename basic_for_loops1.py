# Implementacion de bucle for loop basico.


# for x in range(151):
#     print(x)

# for x in range(5,1001): # funcion for loop para mostrar multiplos de 5 entre 5 a 1000
#     if x % 5 == 0: # si x es divisible por 5, imprimir x
#         print(x)

# for x in range(1,101):
#     if x % 10 == 0:
#         print("Coding Dojo")
#     elif x % 5 ==0:
#         print("Coding")
#     else:
#         print(x)



# y = 0
# for x in range(5):
#     if x % 2 != 0: # si la divison de x por 2 es distinto a 0 ( decimal) es un numero impar
#         y += x # si el if anterior se cumple la variable y ira sumando la iteracion de x que sea impar
# print(y)
### suma final de numeros impares entre 0 a 500000


# # cuenta regresiva de 4 en 4 desde 2018 
# y = 2018 # variable con valor 2018 para iniciar cuenta regresiva
# while y > 0: # mientras y sea mayor a 0, se ejecuta el bloque de codigo
#     print(y) # muestra el valor de y
#     y = y - 4 # asigna un nuevo valor a y, terminando el bloque y yendo al inicio nuevamente.

# lowNum = 1
# highNum = 111
# mult = 22

# for x in range(lowNum,highNum+1): # imprime los valores multiplos ( % ==0) desde lowNum a highNum
#     if x % mult == 0:
#         print(x)