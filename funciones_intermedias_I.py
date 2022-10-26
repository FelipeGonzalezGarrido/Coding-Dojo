import random
def randInt(min=0, max=100):
    num = random.random() * max +min
    return round(num)
print(f"numero aleatorio entre 0 a 100: {randInt()}") # hecho
print(f"numero aleatorio entre 0 y 50  : {randInt(max=50)}")
print(f"numero aleatorio entre 50 y 100: {randInt(min=50,max=50)}")
print(f"numero aleatorio entre 50 y 500: {randInt(min=50,max=450)}")

