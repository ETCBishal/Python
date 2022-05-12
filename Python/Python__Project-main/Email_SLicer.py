'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''

'''
This is besically a program which takes Email a an input
for eg:-
Email:youremail@gmail.com

and it will slice means it separates the domain name of the email address
given by the users and print the user name

'''

EMAIL = input('Email your email address\n> ').strip()

user_name = EMAIL[:EMAIL.index("@")]

domain = EMAIL[EMAIL.index("@")+1:]     # You can notice that wht +1 is written here.
                                        # It is because we are avoiding the "@"(attherate) sign


print(f"Your username is : {user_name}\nAnd domain name is : {domain}")


