# math library import statement
from math import *
num10 = 9.7
print(ceil(num10))
print(floor(num10))

print("Hello, World!")
print("   /|")
print("  / |")
print(" /  |")
print("/___|")

character_name = "John"
character_age = "35"
is_male = True

print(character_name)
print(character_age)

print("There once was a man named " + character_name)
phrase = "String"
print(phrase)
print(phrase.upper())
print(phrase.lower())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))
print(phrase[0])
print(phrase.index("t"))
print(phrase.replace("r", "u"))

print(str(5) + " is a number")
num = -5
print(num)
print(abs(num))
print(pow(num, 2))
print(max(num, 3))
print(min(num, 3))
print(round(98.987))

# get user input
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + " you are " + age)

# make a calculator
# python reads all input in as strings and must be type cast

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

result = int(num1) + float(num2)
print(result)


# mad lib
color = input("Enter a color")
plural_noun = input("Enter a plural noun")
celebrity = input("Enter a celebrity")

print(f"Roses are {color}")
print(f"{plural_noun} are blue")
print(f"I love {celebrity}")

# lists
# type doesn't matter, can mix strings, booleans, or numbers
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tony"]
print(friends)
print(friends[0])
# access last position in list
print(friends[-1])
# access all elements from this position forward
print(friends[1:])
# access all elements in range
print(friends[1:3])
friends[1] = "Mike"
