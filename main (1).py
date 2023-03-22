# This program is a simple calculator

# Define function for addition
def add(x, y):
    return x + y

# Define function for subtraction
def subtract(x, y):
    return x - y

# Define function for multiplication
def multiply(x, y):
    return x * y

# Define function for division
def divide(x, y):
    return x / y

# Take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Ask user to input choice
choice = input("Enter choice (1/2/3/4):")

# Ask user to input values
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Execute chosen operation and print result
if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))
else:
    print("Invalid input")
