#Project Day 1
# print("Welcome to the Band Name Generator.\n")
# city = input("What's the name of the city you grew up in? \n")
# pet = input("What's the name of your first pet \n")
# print(f"Your Band Name is {city} {pet}")

# Project Day 2
# total_bill = float(input("What was the total bill? $\n"))
# percent_tip = float(input("What percentage tip would you like to give? 10, 12, or 15 \n"))
# people = int(input("How many people to split the bill? \n"))
# total = ((total_bill * percent_tip) / 100) + total_bill
# result = total/people
# print(result*people)
# print(f"Each person should pay: ${round(result)}")

# Project Day 3
# print("Welcome to treasure Island. \n")
# print("Your mission is to find the One Piece. \n")
# choice1 = input("You're at a cross road. Where do you want to go?. Type 'left' or 'right' :\n").lower()
# if choice1 == "left":
#     print("You have found the One Piece")
# elif choice1 == "right":
#     choice2 = input("You have encountered some wild animals, they start attacking you. choose betweem 'fight' or 'scape': \n").lower()
#     if choice2 == "fight":
#         print("Fighting the animals makes them more aggresive, you fucking died.")
#     elif choice2 == "scape":
#         print("Nowhere to scape with that big ass belly. You've died")
#     else:
#         print("Your pants are full of excrement, unable to run. The wild animals take a turns to bite your ass")
# else:
#     print("Invalid Choice, you have died")

# Project Day 4
# import random
# rock = '''
#     _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# '''
# paper = '''
#     _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)
# '''
# scissors = '''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# '''
# decision1 = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
# decision2 = random.randint(0,2)
# juego = [rock,scissors,paper]
# if decision2 == decision1:
#     print(f"You choose {juego[decision1]}")
#     print(f"Computador choose {juego[decision2]}")
#     print("It's a Draw.")
# elif decision1 == 0: # PIEDRA
#     print(f"You choose {juego[decision1]}")
#     if decision2 == 1: # TIJERAS
#         print(f"Computador choose {juego[decision2]}")
#         print("You WIN.")
#     else:
#         print(f"Computador choose {juego[decision2]}")
#         print("You Lose.")
# elif decision1 == 1: # tijera
#     print(f"You choose {juego[decision1]}")
#     if decision2 == 2: # papel
#         print(f"Computador choose {juego[decision2]}")
#         print("You WIN.")
#     else:
#         print(f"Computador choose {juego[decision2]}")
#         print("You Lose.")
# elif decision1 == 2: # papel
#     print(f"You choose {juego[decision1]}")
#     if decision2 == 0:
#         print(f"Computador choose {juego[decision2]}")
#         print("You WIN.")
#     else:
#         print(f"Computador choose {juego[decision2]}")
#         print("You Lose.")

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# pass_letters = ""
# pass_symbols = ""
# pass_numbers = ""
# rand = 0
# final = []
# password = ""
# for x in range(0,nr_letters):
#     ran = random.randint(0, len(letters)-1)
#     x = letters[ran]
#     final.append(x)

# for x in range(0,nr_symbols):
#     ran = random.randint(0, len(symbols)-1)
#     x = symbols[ran]
#     final.append(x)

# for x in range(0,nr_numbers):
#     ran = random.randint(0, len(numbers)-1)
#     x = numbers[ran]
#     final.append(x)
# random.shuffle(final)

# for x in final:
#     password += x

# print(password)
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letter = letter + x

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

