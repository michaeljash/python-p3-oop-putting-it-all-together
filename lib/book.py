#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def pick1(self):
        print ("Picked book1")
    def pick2(self):
        print("Picked book2")
    def pick3(self):
        print("Picked book3")
    def pick4(self):
        print("Picked book4")

book1 = Book("Death Row","Michael.B","642")
book2 = Book("Atlas","Jeniffer.L","579")
book3 = Book("World of Apes","Jason","945")
book4 = Book("Debugging","Michael Jashon","756")


book1.pick1()
book2.pick2()
book3.pick3()
book4.pick4()

print(book1)
