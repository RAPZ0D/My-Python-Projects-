#ASSIGNMENT 1
# 1. PALLINDROME STRING OR NOT 
new_string = 'hannah'
if new_string[::-1] == new_string:
    print(f'{new_string} is Pallindrome')
else:
    print(f'{new_string} is not Pallindrome')

#2. COMMON ELEMENTS BETWEEN TWO LISTS
string1 = [5,6,7,8,9]
string2= [1,3,5,7,9]
common = set(string1) & set(string2)
print(f'The common elements are {len(common)}')

#3 TEMPERATURE in FARENHEIT TO CELCIUS
def temperature(c,f):
    farenheit = (c *(9/5)) + 32
    celcius = (f - 32) * (5/9)
    return (farenheit,celcius)
a =int(input('Enter the degrees in Celcius'))
b = int(input('Enter the degrees in Farenheit'))
result_farenheit,result_celcius= temperature(a,b)
print(f'Celcius: {result_celcius} \nFarenheit: {result_farenheit}')

#4 GCD GREATEST COMMON DIVISOR
def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)
num1 =999
num2 =456
gcd_result = gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is {gcd_result}.")

#6 FIBONACCI SERIES 
n = int(input("Enter the number of terms"))
num1 = 0
num2 = 1
next_number = num2 
count = 1
while count <= n:
    print(next_number)
    count += 1
    num1, num2 = num2, next_number
    next_number = num1 + num2

#7 Shortest distance between  two points
import math
def shortest_distance(a,b,c,d):
    distance = math.sqrt((b-a)**2 + (d-c)**2)
    return distance
x1,x2 = 10,15
y1,y2= 12,5
result = shortest_distance(x1,x2,y1,y2)
print(f"The shortest distance between ({x1}, {y1}) and ({x2}, {y2}) is {result:.2f}")

#10 AREA OF CIRCLE RECTANGLE AND TRIANGLE
def Area(a,b,c,d,e):
    circle_area = 3.14 * (a**2)
    rectangle_area = b*c
    triangle_area = 0.5 * d * e 
    return (circle_area,rectangle_area,triangle_area)
radius = float(input('Input the radius'))
length = float(input('Enter the length of the rectangle'))
width = float(input("Enter the width of the rectangle"))
breadth = float(input("Enter the breadth of the triangle"))
height = float(input("Enter the height of the triangle"))

result_circle,result_rectangle,result_triangle = Area(radius,length,width,breadth,height)
print(f"The area of circle is = {result_circle:.2f} \nThe area of rectangle is = {result_rectangle:.2f} \nThe area of the triangle is = {result_triangle:.2f} ")

#5 ATM MACHINE

def atm():
    balance = 0
    while True:
        print("\nATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance Inquiry")
        print("4. Exit")

        input_choice = input("Enter your choice 1/2/3/4: ")

        if input_choice == '1':
            amount_needed = float(input("Enter the deposit amount_needed: $"))
            if amount_needed > 0:
                balance += amount_needed
                print(f"Deposited ${amount_needed}. New balance: ${balance}")
            else:
                print("Invalid amount_needed for deposit.")
        elif input_choice == '2':
            amount_needed = float(input("Enter the withdrawal amount: $"))
            if 0 < amount_needed <= balance:
                balance -= amount_needed
                print(f"Withdrew ${amount_needed}. New balance: ${balance}")
            else:
                print("Insufficient funds or invalid amount for withdrawal.")
        elif input_choice == '3':
            print(f"Current balance: ${balance}")
        elif input_choice == '4':
            print("Thank you for using ATM. Goodbye!")
            break
        else:
            print("Invalid input choice. Please select a valid option.")

if __name__ == "__main__":
    atm()
