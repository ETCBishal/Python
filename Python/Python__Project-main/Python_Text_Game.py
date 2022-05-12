
'''
Text Based Adventure Game
'''

'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali

'''


import time                      #####################################################################################################
from pygame import mixer       # Make sure that the pygame is Installed                                                                # 
                               # If not then copy the code given in the bracket and paste it into your terminal [ pip install pygame ] # 
                                 #####################################################################################################

def next_stp():
    turn_on = ("Do you want to TURN ON the torch light or NOT [yes/no]\n> ").lower()
    if turn_on == "yes" or "y":
        print("Now the room became a little bit bright\n")
        print("There are 3 doors\n1.[Lion] and the lion is hungry from 3 days\n2.If you touch the second door then you may got electric shock and die\n[HINT: There is a wooden stick in front of you]\n3.[SNAKE] The snake is Venomous\n")
        inp = int(input("Which door you want to choose\n1.[LION'S DOOR]\n2.[ELECTRIC SUPPLIED DOOR]\n3.[SNAKE'S DOOR]\n> "))
        if inp == 1:
            print("You die because the hunger lion kill and eat you.")
            print("\t\t\t\t\tGAME OVER")
        
        elif inp == 2:
            pick = int(input("\nWhat you want to do\n1.Pickup the wooden stick\n2.No\n> "))
            if pick == 1:
                print("Congrats! YOU ESCAPED")
            elif pick == 2:
                print("You got electric shock and died")
                print("\t\t\t\t\tGAME OVER !!!")

        elif inp == 3:
            print("You  die because the venomous snake bite you.")
           
        else:
            print("Wrong input! Try again")
            again = input("Do you want to try again [yes/no]\n> ").lower()
            if again == "yes" or "y":
                next_stp()
            elif again == "no" or "n":
                print("OK")
            


def greet():
    print("Loading........")
    time.sleep(2.5) # This will sleep for 2.5 second and executes the downward code
#____________________Playing Music__________________________    
    mixer.init()                # Initializing              |
    mixer.music.load("adv.mp3") # Loading the music         |
    mixer.music.set_volume(0.7) # Setting the volume        |
    mixer.music.play()          # Playing the music         |
#___________________________________________________________|

    print("\t\t\t\t\tWELCOM TO DARK ROOM ESCAPE\n")
    print("\nYou are in a very dark room")
    torch = input("Do you want to pick up the torch light [yes/no]\n> ").lower()
    if torch == "yes":
        next_stp()
    elif torch == "no":
        print("The room is still dark")
        greet()
    else:
        print("Try Again")
        ag = input("Do you want to try again [yes/no]\n> ").lower()
        if ag == "yes" or "y":
            greet()
        elif ag == "no" or "n":
            print("Ok")
        else:
            print("Invalid Input!")

def asking():
    ask_for_play = input("Do you want to play[yes/no]\n> ").lower()

    if ask_for_play == "yes" or "y":
        greet()
    elif ask_for_play == "no" or "n":
        print("Ok")
    else:
        print("Wrong input")
        tryAgain = input("DO you want to try again [yes/no]\n>").lower()
        if tryAgain == "yes" or "y":
            print("\t\t\t\t\tCONTINUE\n")
            asking()
        
asking()


                                                ###########
                                              #  STAY SAFE  #
                                              #     BYE     #
                                                ###########


