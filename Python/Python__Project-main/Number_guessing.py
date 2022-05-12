import random

'''
    This is Number Guessing Game    
    
Creator Details

Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali

'''


if __name__ == '__main__':

    askName = input("Enter your name\n> ").capitalize()  # Asking the user for their name 

    print(f"Wlcome! {askName}") # Greeting the user by their name

    while True:
        # Asking the user to enter teh lower bound of
        low = int(input("\nEnter a number for the lower bound\n> "))
            

        # Asking the user to enter the upper bound number
        up = int(input("\nEnter a number for upper bound\n> "))

        # Asking the user to enter the number of guess they wants
        guess = int(input("\nHow many guess you wants?\n> "))

        # Generating a random number in the bases of user input
        SECRETNUMBER = random.randint(low,up) 

        COUNT = 0

        print(f"You have {guess} guess\n")

        while COUNT < guess: 
            
            TRYGUESS = int(input("Try a guess\n> "))  # Asking to guess a number
            
            
            if TRYGUESS < SECRETNUMBER:     # If the user guess is less
                print("Your guess is less\n")
                COUNT += 1
                print(f"{guess-COUNT} guess left\n")
                
            elif TRYGUESS > SECRETNUMBER:       # If the user guess is higher
                print("Your guess is higher\n")
                COUNT += 1
                print(f"{guess-COUNT} guess left\n")
                
            elif TRYGUESS == SECRETNUMBER:   # If the user guessed the number
                COUNT += 1
                print("You have guessed it in "+str(COUNT)+ " try\n")
                Again = input("Do you want to play again? [y/n]\n> ")
                if Again!="y" or  "yes":
                    break  
                
            else:                            # If user write something else then it will be printin [Invalid Input]
                print("Invalid Input")
                
            
            
