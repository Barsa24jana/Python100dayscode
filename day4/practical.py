'''Rock paper scissors game'''
import random
print("wWelcome to Rock Paper Scissors Game")
user_choice = int(input("What do you choose? Type 1 for Rock , 2 for Paper, 3 for Scissors :"))
computer_choice = random.randint(1,3) #Generate a random number between 1 and 3
print(f"Computer chose: {computer_choice}")
if user_choice == computer_choice:
    print("It's a Draw!")
elif user_choice == 1 and computer_choice == 2:
    print("You lose! Paper covers Rock")
elif user_choice == 1 and computer_choice == 3:
    print("You win! Rock crushes Scissors")
elif user_choice == 2 and computer_choice == 1:
    print("You win! Paper covers Rock")
elif user_choice == 2 and computer_choice == 3:
    print("You lose! Scissors cuts Paper")
elif user_choice == 3 and computer_choice == 1:
    print("You lose! Rock crushes Scissors")
elif user_choice == 3 and computer_choice == 2:
    print("You win! Scissors cuts Paper")
else:
    print("Invalid choice! Please choose 1, 2, or 3.")
    