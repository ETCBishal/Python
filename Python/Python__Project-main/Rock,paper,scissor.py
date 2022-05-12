'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''

import random

ask = input("Do you want to know the rule of this game\n> ").lower()

def game_rule():
    print("Rules:\n|1.Scissor cuts paper\n|2.Paper covers rock\n|3.Rock smash scissor\n   Thank You !!\n")
if ask == "yes":
    game_rule()

action = ["r","p","s"]
chance = 10
no_of_chance = 0
player_point = 0
computer_point = 0

print("Action :\n|1.r for rock   |\n|2.p for paper  |\n|3.s for scissor|\n")

# Making the game in while 
while no_of_chance < chance:
    user = input("Enter an action [rock, paper, scissor]\n> ").lower()
    _random = random.choice(action)

    # If Tie 
    if user == _random:
        print("Tie you both have 0 score\n")
    
    # When user enter r[rock]
    elif user == "r" and _random == "p":
        computer_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    elif user == "r" and _random == "s":
        player_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Win")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    
    # When user enter p [paper]
    elif user == "p" and _random == "r":
        player_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Win")
        print(f"Your score is {player_point} and computer score {computer_point}\n")
    elif user == "p" and _random =="s":
        computer_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")

    # When user enter s [scissor]
    elif user == "s" and _random == "p":
        player_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Win")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    elif user == "s" and _random == "r":
        computer_point += 1
        print(f"You have choosen {user} and computer have choosen {_random}")
        print("You Lose")
        print(f"Your score is {player_point} and computer score is {computer_point}\n")
    
    # If user enter any thisng wrong 
    else:
        print("The input is wrong! Please try Again!")
    
    no_of_chance += 1
    print(f"{chance - no_of_chance} chance is left out of {chance}")

if player_point == computer_point:
    print("Tie\n")

elif player_point > computer_point:
    print("You Own\n")

else:
    print("You Lose and Computer Win")

print(f"Your total score is {player_point} and computer total score is {computer_point}\n")
print("   Thank YOU!\nGame Over... See You Next Time! \n")

