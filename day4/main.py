import random

choices = ["Rock","Paper","Scissor"]

user_choice = int(input("What do you choose? Type 0 for rock,1 for paper,2 for scissor."))
if user_choice < 0 and user_choice > 2:
    print("You put an Invalid Number!")
else:
    computer_choice = random.randint(0, 2)
    print(f"Computer Choice: {computer_choice}")

    print(f"You choose: {user_choice}")
    if user_choice == computer_choice:
        print("It's a Draw")
    elif user_choice == 0 and computer_choice == 2 or\
         user_choice == 1 and computer_choice == 0 or\
         user_choice == 2 and computer_choice == 1:
         print("You Won!")
    else:
        print("You Loose!")