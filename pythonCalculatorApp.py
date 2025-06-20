import math

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b
def power(a, b): return a ** b
def sqrt(a):
    if a < 0:
        return "Error: Negative number!"
    return math.sqrt(a)
def factorial(n):
    if n < 0:
        return "Error: Negative number!"
    return math.factorial(n)

def calculator():
    while True:
        print("\n Calculator Menu:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (x^y)")
        print("6. Square Root")
        print("7. Factorial")
        print("0. Exit")

        choice = input("Select operation (0-7): ")

        if choice == '0':
            print(" Exiting calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5']:
            try:
                a = float(input("Enter first number: "))
                b = float(input("Enter second number: "))
            except ValueError:
                print(" Invalid input. Please enter numeric values.")
                continue

            if choice == '1':
                print("Result:", add(a, b))
            elif choice == '2':
                print("Result:", subtract(a, b))
            elif choice == '3':
                print("Result:", multiply(a, b))
            elif choice == '4':
                print("Result:", divide(a, b))
            elif choice == '5':
                print("Result:", power(a, b))

        elif choice == '6':
            try:
                a = float(input("Enter number: "))
                print("Result:", sqrt(a))
            except ValueError:
                print(" Invalid input.")
        elif choice == '7':
            try:
                n = int(input("Enter integer number: "))
                print("Result:", factorial(n))
            except ValueError:
                print(" Invalid input. Enter a whole number.")
        else:
            print(" Invalid choice. Please choose a valid option.")


calculator()
