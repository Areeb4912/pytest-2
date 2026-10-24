def add(a, b):
    return a +b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

print("====Function Calculator====")
print("1. Addition(+)")
print("2. Subtraction(-)")
print("3. Multiplication(*)")
print("4. Division(/)")

try:
    choice = int(input("Enter your choice (1-4):"))
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    if choice ==1:
        result = add(num1,num2)
        print(result,"is the result of addition")
    elif choice ==2:
        result = subtract(num1,num2)
        print(result,"is the result of subtraction")
    elif choice ==3:
        result = multiply(num1,num2)
        print(result,"is the result of multiplication")
    else:
        result = divide(num1,num2)
        print(result,"is the result of division")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")