import random
import string

print("            }PASSWORD GENERATOR{")


length = int(input("Enter password length: "))

print("\nChoose Password Complexity:")
print("1. Letters Only")
print("2. Letters + Numbers")
print("3. Letters + Numbers + Special Characters")

choice = input("Enter your choice (1-3): ")

if length < 4:
    print("\nPassword length should be at least 4.")

elif choice == "1":
    characters = string.ascii_letters

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    if length < 6:
        print("Password Strength: Weak")
    elif length < 10:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")

elif choice == "2":
    characters = string.ascii_letters + string.digits

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    if length < 6:
        print("Password Strength: Weak")
    elif length < 10:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")

elif choice == "3":
    characters = string.ascii_letters + string.digits + string.punctuation

    password = ""
    for i in range(length):
        password += random.choice(characters)

    print("\nGenerated Password:", password)

    if length < 6:
        print("Password Strength: Weak")
    elif length < 10:
        print("Password Strength: Moderate")
    else:
        print("Password Strength: Strong")

else:
    print("\nInvalid choice. Please select 1, 2, or 3.")
