'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''


#--------------- Defining a function and importing datetime Module-----------------
def getdate():
    import datetime
    return datetime.datetime.now()


#------------------------ Defining log function ------------------------------------
def log():
    print("1.Harry")
    print("2.Rohan")
    print("3.Hammad")
    clt_number = int(input("Enter a clt_number\n> "))

    
#----------------- To log smoeting--------------------------------------------------
    if clt_number == 1:
        print("1.Food")
        print("2.Exercise")
        log_number = int(input("What you wnat to log to Harry\n> "))

                
        if log_number == 1:
            print("Log food name = ", end="")
            with open("Harry-food.txt", "a") as harry_file:
                harry_file.write('['+str(getdate())+']' + " " + input() + "\n")

        elif log_number == 2:
            print("Log exercise name = ",end="")
            with open("Harry-Exercise.txt","a") as harry_file:
                harry_file.write('['+str(getdate())+']' + " " + input() + "\n")
        else:
            print('!Input ERROR!')

    elif clt_number == 2:
        print("1.Food")
        print("2.Excer")
        log_number = (input("What you want to log to Rohan\n> "))
        

        if log_number == 1:
            print("Log food name = ", end="")
            with open("Rohan-food.txt","a") as rohan_file:
                rohan_file.write('['+str(getdate())+']' + " " + input() + "\n")
        elif log_number == 2:
            print("Log Exercise naem = ",end="")
            with open("Rohan-Exercise.txt","a") as rohan_file:
                rohan_file.write('['+str(getdate())+']' + " " + input() + "\n")

        else:
            print("!Input Error!")

    elif clt_number == 3:
        print("1.Food")
        print("2.Exercise")
        log_number = (input("What you want to log to Hammad\n> "))
        if log_number == 1:
            print("Log food name :",end="")
            with open("Hammad-food.txt",'a') as hammad_file:
                hammad_file.write('['+str(getdate())+']' + " " + input() + "\n")

        elif log_number == 2:
            print("Log Exercise name :",end="")
            with open("Hammad-Exercise.txt","a") as hammad_file:
                hammad_file.write('['+str(getdate())+']' + " " + input() + "\n")
        else:
            print("Invalid Number is Entered!\nPlease Check Your Input!")
    
    else:
        print(f"No Clint Existing clt_number {clt_number}")

#------------------- To Read Already Saved File-----------------------------
def fetch():
    print("Clint List:-")
    print("1.Harry")
    print("2.Rohan")
    print("3.Hammad")
    print("Of which clint data u want to fetch :",end="")
    clt_number = int(input())
    if clt_number == 1:
        print("Data List:-")
        print("1.Food")
        print("2.Exercise")
        log_number = int(input("Enter a log_number\n> "))
        if log_number == 1:
            with open("Harry-food.txt") as f:
             print(f.read())
            
        elif log_number == 2:
            with open("Harry-Exercise.txt") as f:
                print(f.read())

        else:
            print("Sorry! Invalid Log")


    elif clt_number == 2:
        print("Data List:-")
        print("1.Food")
        print("2.Exercise")
        log_number = int(input("Enter a log_number\n> "))
        if log_number == 1:
            with open("Rohan-food.txt") as f:
                print(f.read())
        
        elif log_number == 2:
            with open("Rohan-Exercise.txt") as f:
                print(f.read())
        
        else:
            print("Sorry! Invalid Log")

    elif clt_number == 3:
        print("Data List:-")
        print("1.Food")
        print("2.Exercise")
        log_number = int(input("Enter a log_number\n> "))
        if log_number == 1:
            with open("Hammad-food.txt") as f:
                print(f.read())

        elif log_number == 2:
            with open("Hammad-Exercise.txt") as f:
                print(f.read())

        else:
            print("Sorry! Invalid Log")


#------------------------- Calling The Function acording to the user --------------------
    
print("1.Log\n2.Fetch")
do = int(input("What you want to do\n> "))
if do == 1:
    log()

elif do == 2:
    fetch()

else:
    print("Please check your Input!")

#--------------------------- Program Ended :) -------------------------------------------
