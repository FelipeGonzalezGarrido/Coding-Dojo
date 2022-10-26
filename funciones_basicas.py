#1
def a():
    return 5
print(a())
# Prediccion:  5, es el valor de return de la funcion

#2
def a():
    return 5
print(a()+a())
# Prediccion: 10 es la suma del valor return de la funcion

#3
def a():
    return 5
    return 10
print(a())
# Prediccion: 5, es el primer return de la funcion, los demas se omiten

#4
def a():
    return 5
    print(10)
print(a())
# Prediccion: 5, el return no permitira la ejecucion de print

#5
def a():
    print(5)
x = a()
print(x)
# Prediccion: 5  /n None, se llama la funcion la cual muestra 5 con print y luego el  valor de la funcion el cual es None al no tener un return.

#6
def a(b,c):             
    print(b+c)          
print(a(1,2) + a(2,3))  
# Prediccion:  8. resultado de la suma dentro de ambas funciones.

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Prediccion: 25. Concatenacion de numeros transformados a string en sentencia return

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Prediccion: 100 /n 10. ignorando problema de indentacion. la funcion mostrara valor de b y return en else.

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Prediccion: 7 /n 14 /n 21. dados los valores de funcion, 2<3 = True 7, 5< 3 = False 14. 2< 3 = True 7 + 5< 3 = False 14 (21)

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Prediccion: 8, llamado a funcion a() indica argumentos 3 y 5 los cuales se suman en sentencia return.

#11
b = 500
print(b)
def a(): 
    b = 300
    print(b)
print(b)
a()
print(b)
# Prediccion: 500 /n 500 /n 300 /n 500. funcion print muestra el valor de b, b, llama a funcion la cual muestra valor asignado de 300, y fuera de funcion valor de b nuevamente.

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Prediccion: 500 /n 500 /n 300 /n 500. similar a la anterior. la sentencia return b de la funcion no es solicitada para mostrar, aunque si es calculada.

#13
b = 500
print(b) # 500
def a():
    b = 300
    print(b)
    return b
print(b) # 500
b=a()
print(b) # 300 /n 300
# Prediccion: 500 /n 500 /n 300 /n 300. funcion se almacena en variable b para luego ser llamada por print. la cual ejecuta print almacenado en funcion y retorna valor de funcion

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# Prediccion:  1 /n 3/n 2. funcion a() realiza print a, llama a funcion b la cual muestra el valor 3 con print, y por ultimo realiza print 2

#15
def a():
    print(1) 
    x = b()
    print(x) 
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Prediccion: 1 /n 3 /n 5 /10 .  funcion a() muestra valor 1, asigna la funcion b() a variable x, llama a variable x mostrando print 3 y valor 5 por ultimo retorna valor 10.








