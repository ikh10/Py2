# Understanding the terms define, call, pass, argument, and parameter.
import sys

def Main(): # Define
    while True:
        print("Simple Calculator \n")
        print("1. Add")
        print("2. Sub")
        print("3. Mul")
        print("4. Div")
        print("5. Exit Program")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            calculator("add") # Arguments
        elif choice == '2':
            calculator("subtract")
        elif choice == '3':
            calculator("multiply")
        elif choice == '4':
            calculator("divide")
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid option. Try again.")

def calculator(operation): # Parameter
    while True:
        
        num1 = float(input("Enter first num: "))
        

        
        num2 = float(input("Enter second num: "))
        

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                print("Can't divide by zero.")
                continue
            result = num1 / num2
        else:
            result = None

        print("Result:", result)
       sys.exit() # Exit

# Run the calculator
Main() # Calling
