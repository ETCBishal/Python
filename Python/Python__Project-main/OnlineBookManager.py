'''
Creator Details
Name : Bishal jaiswal
Class : VIII(8)
Nationality : Nepali
'''

print("Welcome to the Book manager")

class Library:
    dict1 = {}
    def __init__(self,list):
        self.list = list
    @staticmethod
    def start():
        print("1.Display the book\n2.Lend boik\n3.Add a new book\n4.Return the book")
    
    def display(self):
        return f"The available books are\n{self.list}"
    def lend(self):
        print(f"The available books are\n{self.list}")
        book = input("Please enter the name of the book you want to lend\n> ")
        user_name = input("Please enter your name\n> ").capitalize()
        if book in self.list:
            if book not in self.dict1.keys():
                self.dict1.update({book:user_name})
                return f"Done! you can now lend {book}"

            else:
                return f"The book is already owned by {self.dict1[book]}"
        else:
            return f"Sorry the book you entered is not available in our library"
        
    def addd(self):
        name_of_book = input("Enter the name of the book you want to add\n> ")
        self.list.append(name_of_book)
        return f"Successfully added {name_of_book} book!"
    def returnn(self):
        returnbook=input("Enter which book do you want to return\n> ")
        returnname=input("Enter your name\n> ").capitalize()
        if returnbook in self.dict1.keys() and returnname in self.dict1.values():
            self.dict1.pop(returnbook)
            return f"Successfully returned the book."
        else:
            return f"Sorry {returnname} you have not lent {returnbook}"

Dictionary = Library(["Cracking the code","Hacking the database","Shield to the earth"])
while True:
    Dictionary.start()
    ask = input("What do you want to do?\n> ")
    if ask == "1":
        print(Dictionary.display())
    elif ask == "2":
        print(Dictionary.lend())
    elif ask == "3":
        print(Dictionary.addd())
    elif ask == "4":
        print(Dictionary.returnn())
    else:
        print("Wrong input")
    
    Ask_for_cintinue = input("Do you want to continue [y/n]\n> ").lower().strip()
    if Ask_for_cintinue == "y":
        continue
    elif Ask_for_cintinue == "n":
        exit()
    else:
        print("Type only [ y or n ]")
