#LAB 2
# PYTHON FUNCTIONS
#1 List even numbers 
def even():
    new_list = [2,3,4,5,6,7,8]
    even_list = []
    for num in new_list:
        if num % 2 == 0:
            even_list.append(num)
    print("The list of even numbers is: ", even_list)
even()
#2 Area of Triangle 
def triangle(a,b):
    area = 0.5 * a * b
    return area
length = float((input('Enter the Length')))
height = float(input("Enter the height"))
result = triangle(length,height)
print(f"The area of the triangle is: {result}")

#3 Celcius to farehneit
def temperature():
    f = float(input("Enter the temperature in Fahrenheit: "))
    c = (f - 32) * 5/9
    print("The temperature in Celsius is: ", c)

temperature()

#5 GCD 
def GCD():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    while b:
        a, b = b, a % b
    print("The GCD is: ", a)
GCD()

# OBJECT ORIENTED PROGRAMMING
# 2 Shape
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width, self.height = width, height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (length+height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14 * self.radius

rectangle = Rectangle(3,6)
circle = Circle(7)
print(f"Area of Rectangle: {rectangle.area()} \n Perimeter is : {rectangle.perimeter()}")
print(f"Area of Circle: {circle.area()}\n Perimeter is: {circle.perimeter()}")

# BIRD MAMMAL
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def fly(self):
        pass
    def give_birth(self):
        pass
class Bird(Animal):
    def fly(self):
        return f"{self.name} has started to FLY!!"
class Mammal(Animal):
    def give_birth(self):
        return f"{self.name} Has given Birth!!"
    
def get_animal_info():
    name = input("Enter the name of the animal: ")
    age = input("Enter the age of the animal: ")
    return name, age

def create_animal():
    animal_type = input("Select animal type (Bird/Mammal): ").strip().lower()
    name, age = get_animal_info()
    if animal_type == "bird":
        return Bird(name, age)
    elif animal_type == "mammal":
        return Mammal(name, age)
    else:
        print("Invalid animal type")
        return None
animal = create_animal()
if animal:
    print(f"{animal.name} is {animal.age} years old.")
    print(animal.give_birth())
    print(animal.fly())

#MODULES
# 1 BASIC ARITHEMETIC OPERATIONS
import calculator
print("The sum is : {}".format(calculator.add(50,10)))
print("The subraction is : {}".format(calculator.subtract(50,10)))
print("The multiplication is : {}".format(calculator.multiply(50,10)))
print("The division is : {}".format(calculator.divide(50,10)))

# 4 API REQUESTS
import requests
response = requests.get("https://randomuser.me/api/")
response.text

# 5 string_utils
import string_utils
print('the reversed string is: {}'.format(string_utils.reverse_string(a='string a')))
print('the counting is: {}'.format(string_utils.counting(a='string a')))
print('the Uppercase string is: {}'.format(string_utils.uppercase(a='string a')))

# FILE OPERATIONS

import files_function
filename = "hello.txt"
file_content = files_function.read_file(filename)
print("File Content:")
print(file_content)
new_content = file_content.replace("old_text", "new_text")
result = files_function.write_file(filename, new_content)
print(result)

