'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''



str = input("Enter the number of your credit card\n> ") 
length = len(str)     # It will find the length of the given input by the user. 
mark = length-4       # It will subtract 4 from the length of the given input
hide = str[mark:]     
print(hide)
print("*"*mark+hide)
