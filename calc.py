first_number = float(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /): ")
second_number = float(input("Enter second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":          
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Division by zero is not allowed."
else:    result = "Error: Invalid operation."   
print("Result:", result)