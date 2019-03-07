# Simple Calculator
# This is a program that works as a Simple Calculator.

# These allow us to use the 4 fundamental operations.

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


print("Please select operation.")
print("To add two numbers, press '1'")
print("To subtract two numbers, press '2'")
print("To multiply 2 numbers, press '3'")
print("To divide 2 numbers, press '4'")

# Take input from the user.
choice = input("Enter choice(1,2,3,4):")

num1: int = int(input("Enter first number"))
num2: int = int(input("Enter second number"))

if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2),)

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == "4":
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid Input")
