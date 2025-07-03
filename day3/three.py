'''Control Flow with if /else statement'''
'''Treasure Island'''
picture = '''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************'''
print(picture)
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
print("You are at the cross road.")
step_1 = input("Where do you want to go? Type left or right:\n")
if step_1 == "left":
    print("yahoo! You can go ahead.")
    print("Oops! There's a big lake infront of you.")
    step_2 = input("What do you want? wait or swim:\n")
    if step_2 == "wait": #Nested if statement
        print("Ok! You can go ahead")
        print("Hey! You have reached the Island successfully.\nBut there's three door infront of you.")
        step_3 = input("Which door you want choose? red,blue or yellow:\n")
        if step_3 == "yellow":
            print("Yahoo! You have win the game. Congarts💃🕺")
        else:
            print("oops!You have chosen wrong, game over")
    else:
        print("You have eaten by a crocodile. Game Over")
else:
    print("Game Over")

