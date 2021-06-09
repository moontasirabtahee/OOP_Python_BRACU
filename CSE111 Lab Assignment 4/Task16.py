# Created by Moontasir Abtahee at 6/5/2021

class Author:
    def __init__(self, name="Default", *books):
        self.name = name
        self.book = books

    def addBooks(self, *book):
        self.book = book

    def changeName(self, x):
        self.name = x

    def printDetails(self):
        print(f"Author Name: {self.name}\nList of books: {self.book}")



auth1 = Author('Humayun Ahmed')
auth1.addBooks('Deyal', 'Megher Opor Bari')
auth1.printDetails()
print('===================')
auth2 = Author()
print(auth2.name)
auth2.changeName('Mario Puzo')
auth2.addBooks('The Godfather', 'Omerta', 'The Sicilian')
print('===================')
auth2.printDetails()
print('===================')
auth3 = Author('Paolo Coelho', 'The Alchemist', 'The Fifth Mountain')
auth3.printDetails()