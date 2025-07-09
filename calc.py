def calculator():
    print("Basic Calculator")
    print("Operations available:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    while True:
        try:
            # Get user input
            choice = input("Enter operation number (1/2/3/4) or 5 to exit: ")
            
            if choice == '5':
                print("Exiting calculator. Goodbye!")
                break
            
            if choice not in ('1', '2', '3', '4'):
                print("Invalid input. Please try again.")
                continue
            
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Perform calculation based on user choice
            if choice == '1':
                print(f"Result: {num1} + {num2} = {num1 + num2}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {num1 - num2}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {num1 * num2}")
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero is not allowed.")
                else:
                    print(f"Result: {num1} / {num2} = {num1 / num2}")
            
            print()  # Add empty line for better readability
            
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Run the calculator
calculator()
