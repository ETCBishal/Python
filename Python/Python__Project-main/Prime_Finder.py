'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''


while True:

    ask_num = int(input("Enter a number: "))

    if ask_num%2 == 1:
        print("It is a prime number.")

    elif ask_num%2 == 0:
        print("The number you entered is not a prime number \nbut it's an even number.")

    else:
        print("Wrong Input.")
        
    Again = input("Do you want to try again?\n> ").lower()
    
    if Again !="yes":
        break
