# price = 10
# item = 2
# rating = 4.9
# is_published = True
# print(price + item * rating)
#
# name = 'John Smith'
# age = 20
# is_new = True

# name = input('What is your name? ')
# favcolor = input('What is yur favourite color? ')
# print(name + ' likes ' + favcolor)

# birth_year = input('Birth year: ')
# age = 2023 - int(birth_year)
# print(age)

# weight_lbs = input('Weight (lbs)')
# weight_kg = int(weight_lbs) * 0.45
# print(weight_kg)

# bname = input('what is your brand name ')
# pet = input('what is your pet name ')
# print('Your brand name is ' + bname + " " + pet)

       # CONDITION STATEMENT

# number = int(input("Type in a number "))
# if number % 2 == 0:
#     print(f"{number} is an even number")
# else:
#     print(f"{number} is an odd number")
#     print(number)

# age = int(input("Enter you age\n"))
# height = int(input("What is your height\n"))
# rq_height = 120
# rq_age = 18
# if age >= 18:
#     if height >= 120:
#         print("You are qualify for the tournamrnt")
#     else:
#         print("Oops, your height does not qualify")
# else:
#     print(f"Sorry, come back when you turn {rq_age} and above, and make sure you are {rq_height}cm or more taller")

# if height >= 120:
#     print("You can ride a Rollercoaster.")
#     if age < 12:
#         print("Please pay $5.")
#     elif age <= 18:
#         print("Please pay $12")
# else:
#     print("Sorry you have to grow taller before you can ride")



  # BNI calculator 2.0

# heaght = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))
# bmi = round(weight / heaght ** 2)
# if bmi < 18.5:
#     print(f"Your bni is {bmi}, you are underweight.")
# elif bmi < 25:
#     print(f"Your bni is {bmi}, you are normal weight.")
# elif bmi < 30:
#     print(f"Your bni is {bmi}, you are overweight.")
# elif bmi < 35:
#     print(f"Your bni is {bmi}, you are obese.")
# else:
#     print(f"Your bni is {bmi}, you are clinically obese.")



# Leap year
# year = int(input("Which year do you want to check? "))
#
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#           print("Leap year")
#         else:
#           print("Not a leap year")
#     else:
#         print("leap year")
# else:
#     print("Not a leap year")


# if statement succession

age = int(input("Enter you age \n"))
height = int(input("What is your height\n"))
rq_height = 120
rq_age = 18
bill = 0
if age >= 18:
    if height >= 120:
        print("You are qualify for the tournamrnt")
    else:
        print("Oops, your height does not qualify")
else:
    print(f"Sorry, come back when you turn {rq_age} and above, and make sure you are {rq_height}cm or more taller")

if height >= 120:
    print("You can ride a Rollercoaster.")
    if age < 12:
        amount = 5
        print(f"Please pay ${amount}")
        if age < 12:
            photo = int(input("Want photos"))
            total = photo + amount
            print(f"Your total bill is ${total}")
        else:
            print(f"The total bill is ${amount}")
    elif age < 18:
        print("Please pay $7")
    elif age >= 18:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride")