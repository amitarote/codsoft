print("MENU")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    operation = int(input("Enter your choice: "))

    if operation == 5:
        print("Exiting the calculator. Goodbye!")
        break

    op1 = int(input("Enter operand one: "))
    op2 = int(input("Enter operand two: "))

    if operation == 1:
        add_result = op1 + op2
        print("The addition of given numbers is:", add_result)
    elif operation == 2:
        sub_result = op1 - op2
        print("The subtraction of given numbers is:", sub_result)
    elif operation == 3:
        mul_result = op1 * op2
        print("The multiplication of given numbers is:", mul_result)
    elif operation == 4:
        if op2 != 0:
            div_result = op1 / op2
            print("The division of given numbers is:", div_result)
        else:
            print("Error: Division by zero.")
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")

