# Function to perform arithmetic operations
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:  # Check for division by zero
            return num1 / num2
        else:
            return "Cannot divide by zero"
    else:
        return "Invalid operator"

# Input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")

    # Calculate and display the result
    result = calculate(num1, num2, operator)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter valid numbers.")
except Exception as e:
    print("An error occurred:",e)