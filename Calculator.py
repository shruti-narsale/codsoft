def calculator():
    """Performs basic arithmetic operations based on user input."""

    while True:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            operation = input("Enter operation (+, -, *, /): ")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                result = num1 / num2
            else:
                print("Invalid operation. Please try again.")
                continue

            print("Result:", result)

            another_calculation = input("Do you want to perform another calculation? (y/n): ")
            if another_calculation.lower() != "y":
                break
                print("ok sir") 

        except ValueError:
            print("Invalid input. Please enter numbers only.")
        except ZeroDivisionError as e:
            print(e)

calculator()
