#BASIC CALCULATOR
from art import logo
from replit import clear

#Define the mathematical operations
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#Create dictionary of operations
operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
def calculator():
    print(logo)
    
    #User number input
    num1 = float(input("What's the first number?: "))
    
    #Loop through dictionary and print out operators for user to choose from:
    print("\n")
    for symbol in operations:
        print(symbol)
    
    should_continue = True
    while should_continue:
        operation_symbol = input("\nPick an operation: ")
        #Further user number input
        num2 = float(input("What's the next number?: "))
        
        #Perform the calculation and print the result
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
    
        #Should continue?
        keep_going = input(f"\nType 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:").lower()
        if keep_going == "y":
            num1 = answer
        elif keep_going == "n":
            should_continue = False
            clear()
            calculator()

calculator()