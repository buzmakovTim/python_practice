from math import *
# First Practice with Python!!!

# For comments using '#'

#=======================================================================#
# Variables
#=======================================================================#

# Data Types

# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

first_name = 'Tim'
last_name = 'Buzmakov'

print('Hello ' + first_name + ' ' + last_name)

#################################################
# string functions
phrase = 'Hello Tim'
print(phrase.upper()) # All upper - HELLO TIM
print(phrase.lower()) # All lower - hello tim
print(phrase.isupper()) # return FALSE

#################################################
# numbers functions
print(2)
print(2.3)
print(-3)
print(3+5)
print(5 % 2)  # modules operator %   will print remainder
print(round(3.5))
# for some of functions we need to import modules  ( from math import * )
print(floor(4.6))
print(sqrt(36))

print("##########################################################################")
print("Inputs from user")
print("##########################################################################")
# name = input("Enter your name: ")  # Input data from user
# age = input("Enter your age: ")
# print("Hello " + name + ", your are " + age + "!")

#calculator

# num1 = input("Enter a number: ")
# num2 = input("Enter another number: ")
# result = num1 + num2            # this way Python will treat this input st a string. We need to convert to int or float
# result = int(num1) + int(num2)  # this gonna for only with whole integer
# result = float(num1) + float(num2)  # for this we can use decimal as well

# print("Result is: " + str(result)) # we also have to convert to string as we cant concatenate string and int


print("##########################################################################")
print("List")
print("##########################################################################")

lucky_numbers = [5, 7, 4, 8, 43, 65, 22, 76]
friends = ["Kevin", "Paul", "Dima", "John", "Dima", "Oleg"]

friends[0] = "Alex"
print(friends[2])
print(friends)

# Accessing from the end of the list by using negative values
print(friends[-1])  # will print last element

# Select range
print(friends[1:3])  # range from element 1 to element 3(not included)
print(friends[1:])  # prints all element starting from element 1

# Append one list to another
friends.extend(lucky_numbers)  # two list
friends.append("One Element")  # One element added to the list ALWAYS AT THE END
friends.insert(1, "Tim")  # Adding element at the position 1
friends.remove("John")  # Remove the name
# friends.clear()  # remove all
friends.pop()  # remove last element
print(friends.index("Dima"))  # Prints the index. If not found will be Error
print(friends.count("Dima"))  # Will print number of this elements

# Sort
lucky_numbers.sort()
print(lucky_numbers)
lucky_numbers.reverse()
print(lucky_numbers)

# Copy
friends2 = friends.copy()

print(friends)
print(friends2)


print("##########################################################################")
print("Tuples")
print("##########################################################################")
# Tuple CAN NOT BE CHANGE  it's Immutable

coordinates = (4, 5)

print(coordinates[0])  # Prints 4
print(coordinates)

print("##########################################################################")
print("Dictionary")
print("##########################################################################")
# Pare of value
monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Dec"])



print("##########################################################################")
print("Functions")
print("##########################################################################")
# keyword for function 'def'

def say_hi(name, age):  # naming good practice lowercase
    print("Hello " + name + " you are " + age)

say_hi("Tim", "34")
say_hi("Steve", '36')

# Return statement
def cube(num):
    return num*num*num

print(cube(3))


print("##########################################################################")
print("If Statements")
print("##########################################################################")
is_male = True
is_tall = True

if is_male or is_tall:  # and/or
    print("You are a male or tall or both")
elif is_male and not(is_tall): # elif - else if
    print("You are short male")
else:
    print("You neither male nor tall")

# Comparison in If statements
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(34, 66, 755))