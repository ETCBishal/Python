'''
PASSWORD GENERATOR
'''


'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''


import random
import string

if __name__ == "__main__":
    print(random.__doc__)
    
    ch1 = string.ascii_uppercase
    ch2 = string.ascii_lowercase
    ch3 = string.digits
    ch4 = string.punctuation
    
    pass_length = int(input("Enter the length of the passwords\n> "))
    
    pas = []
    pas.extend(list(ch1))
    pas.extend(list(ch2))
    pas.extend(list(ch3))
    pas.extend(list(ch4))
    
    random.shuffle(pas)
    print("YOur password is > ",end="")
    print("".join(pas[0:pass_length]))
   
