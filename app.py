# print ("Pierre Edouard Fils")
# print("o----")
# print(" ||||")
# print("*" * 10)


# variables
# price =10
# rating = 4.9
# name = "Pierre"
# is_published = True
# print(price)

# full_name = " John Smith"
# age =20
# is_new = True

# Getting Input
# name= input("What is your name ? ")
# # print("Hi "+ name)
# color = input ("What is your favorite color ")
# print(name + " likes " + color)


# Type  Conversion
# birth_year = input("Birth year : ")
# print(type(birth_year))
# age = 2019 -  int (birth_year)
# print(type(age))
# print(age)

# weight_lbs = input("Weight (lbs) : ")
# weight_kg = int (weight_lbs)  * 0.45
# print(weight_kg)

# String
# course = "Python for for Beginners"
#another = course[1:]
#print(another)
#name = "Jennifer"
# print(name [1:-1])

#  Formatted String
# first= 'John'
# Last ='Smith'
# message = first + '[' + Last + '] is a coder '
# msg = f'{first}[{Last}]  is a coder '
# print(msg)

#   String Method
# course = "Python for for Beginners"
# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('Beginners'))
# print(course.replace('Beginners','Absolute Beginners'))
# print('Python 'in course)

# Arithmetic Operations
# print (10 ** 3)
# x = (10 +3) * 2 **2
# x = (2+3) * 10 - 3

# x = x+3
# x -= 3
# print(x)

# Math Functions
# x=2.9
# print(round (x))
# print (abs(-2.9))
# import math
# print (math.floor(2.9 ))

# IF statement
# is_hot = False
# is_cold =False
# if is_hot:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif is_cold:
#     print("It's a cold day")
#     print("Wear warm clothes")
# else :
#     print("It's a lovely day")
#
# print("Enjoy your day ")

# price_house = 1000000
# buyer_credit = True
# if buyer_credit:
#     down_payment = price_house *0.1
# else:
#     down_payment = price_house * 0.2
# print(f"Down payment :${down_payment}")


# Logical operators
# has_good_credit = True
# # has_high_income = False
# #
# # if has_good_credit or has_high_income :
# #     print("Eligible for loan ")
# has_criminal_records = True
#
# if has_good_credit and not has_criminal_records :
#     print("Eligible for loan")

# Comparaison operators
#
# temperature = 30
#
# if temperature > 30 :
#     print("It's a hot day")
# else:
#     print("It's not a hot day")

# name = "John Smith"
# if  len(name)< 3 :
#     print ("Name must be at least 3 Characters")
# elif len(name) >50 :
#     print ("Name must be at  maximum of 50 Characters")
# else:
#     print ("Name look good")

# Project Weight Converter

#
# weight =  int (input("Weight :"))
# measure =input("(L) bs or (k) g :")
# if measure.upper() =="L"  :
#     converted = weight  * 0.45
#     print (f"You are {converted} kilos ")
# else :
#     converted = weight / 0.45
#     print(f"You are {converted} pounds ")

# While loops


# i=1
# while i<= 5:
#     print('*'* i)
#     i=i+1
# print("Done")

# Guessing Game
# secret_number=9
# guess_count = 0
# guess_limit =3
# while guess_count < guess_limit:
#     guess =  int (input("Guess : "))
#     guess_count += 1
#     if guess == secret_number:
#         print("You won")
#         break
# else :
#     print("Sorry You failed ")

# Car Game
# command = ""
# started = False
# while True:
#     command = input(">").lower()
#     if command == "start":
#         if started :
#             print (" Car is already started !")
#         else :
#             started =True
#             print(" Car started...")
#     elif command == "stop":
#         if  not started :
#             print (" Car is already stopped !")
#         else:
#             started = False
#             print(" Car stopped.")
#     elif command == "help":
#         print("""
# start-to start the car
# stop- to stop the car
# quit - to exit
#               """)
#     elif command == "quit":
#
#         break
#     else :
#         print(" Sorry ,I don't understand that")


# For loops
#
# for item in range (10):
#     print (item)

prices = [10, 20, 30]

total = 0
for price in prices:
    total += price
    # print(f"Total:{total} ")
    print(total)