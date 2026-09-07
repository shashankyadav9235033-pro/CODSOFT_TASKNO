num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
print("5. Modulus (%)")
print("6. Power (**)")

choice = input("Enter your choice (1-6): ")

if choice == "1":
    result = num1 + num2
    print(f"\nResult: {num1} + {num2} = {result}")

elif choice == "2":
    result = num1 - num2
    print(f"\nResult: {num1} - {num2} = {result}")

elif choice == "3":
    result = num1 * num2
    print(f"\nResult: {num1} * {num2} = {result}")

elif choice == "4":
    if num2 == 0:
        print("\nError: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"\nResult: {num1} / {num2} = {result}")

elif choice == "5":
    if num2 == 0:
        print("\nError: Cannot perform modulus by zero.")
    else:
        result = num1 % num2
        print(f"\nResult: {num1} % {num2} = {result}")

elif choice == "6":
    result = num1 ** num2
    print(f"\nResult: {num1} ** {num2} = {result}")

else:
    print("\nInvalid choice. Please select 1-6.")

print("\nThank you for using Calculator!")
