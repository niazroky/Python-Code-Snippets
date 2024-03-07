def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero"

while True:
    num1 = float(input("Enter the first number: "))
    operator = input("Enter the operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    result = calculate(num1, num2, operator)

    if isinstance(result, float):
        print(f"Result: {result:.2f}")
    else:
        print(result)

    user_choice = input("Do you want to continue (y/n)? ").lower()

    if user_choice != 'y':
        print("Exiting the calculator.")
        break
