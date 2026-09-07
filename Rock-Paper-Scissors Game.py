import random

print("")
print("       ROCK PAPER SCISSORS GAME")
print("")

user_score = 0
computer_score = 0

while True:

    print("\nChoose your option:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        user_choice = "Rock"

    elif choice == "2":
        user_choice = "Paper"

    elif choice == "3":
        user_choice = "Scissors"

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
        continue

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    print("\nYour choice:", user_choice)
    print("Computer choice:", computer_choice)

    if user_choice == computer_choice:
        print("Result: It's a Tie!")

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        print("Result: You Win!")
        user_score += 1

    else:
        print("Result: Computer Wins!")
        computer_score += 1

    print("")
    print("Your Score:", user_score)
    print("Computer Score:", computer_score)
    print("")
    again = input("\nDo you want to play again? (yes/no): ")

    if again.lower() != "yes":
        break

print("")
print("             FINAL SCORE")
print("")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("Congratulations! You are the winner!")

elif computer_score > user_score:
    print("Computer is the winner!")

else:
    print("The game ended in a tie!")

print("\nThank you for playing!")