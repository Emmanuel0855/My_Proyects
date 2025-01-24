# Function to add two numbers
def add_two_numbers(a, b):
    return a + b

# Function to print n number of asterisks (*)
def print_asterisks(n):
    print('*' * n)

# Function to identify if a number is odd or even
def is_odd(number):
    if number % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

# Main code to call the functions
if __name__ == "_main_":
    # Input for adding two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    result = add_two_numbers(num1, num2)
    print(f"Sum of {num1} and {num2} is: {result}")
    
    # Input for printing asterisks
    n = int(input("Enter number of asterisks to print: "))
    print_asterisks(n)
    
    # Input for checking if a number is odd or even
    number = int(input("Enter a number to check if it's odd or even: "))
    print(is_odd(number))