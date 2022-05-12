'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''


import random

ask_for_rule = input("Do you want to know the rules\n> ").lower()
def rules():
    print("\n|1.Snake drink the water\n|2.Gun kills snake\n|3.Gun drown in water\n   |Thank You !|\n\n")
if ask_for_rule == "yes":
    rules()

lst = ["s","w","g"]

no_of_chance = 0
chance = 10
player_point = 0
computer_point = 0

print("\t\t\t|Snake, Water and Gun|\n\n")

print("Actions:\n|s for snake|\n|w for water|\n|g for gun  |\n")

# Making game in while 

while chance>no_of_chance:
    user = input("Enter a choice [snake,water,gun]\n> ").lower()
    computer = random.choice(lst)

    # Tie 
    if user == computer:
        print("Tie! Both have 0 score")
    
    # When user choose s 
    elif user == "s" and computer =="w":
        player_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You win")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")        
    elif user == "s" and computer == "g":
        computer_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")

    # When user chooes w
    elif user == "w" and computer == "s":
        computer_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    elif user == "w" and computer == "g":
        player_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You Win")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")

    # When user chose g 
    elif user == "g" and computer == "w":
        computer_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    elif user == "g" and computer == "s":
        player_point += 1
        print(f"You guess {user} and computer guess {computer}")
        print("You Win")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")

    # When user input any other 
    else:
        print("Wrong Input is Giver !!")

    no_of_chance += 1
    print(f"{chance-no_of_chance} is left out of {chance}\n")

if player_point == computer_point:
    print("Tie")

elif player_point > computer_point:
    print("Congrats...You Own")

else:
    print("You Lose and Computer Own")

print(f"Your score is {player_point} and computer score is {computer_point}\n")
