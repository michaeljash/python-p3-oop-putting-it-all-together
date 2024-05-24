#!/usr/bin/env python3

class Shoe:
    brand = "Loui.V"
    def __init__(self,name,size,color):
        self.name = name
        self.size = size
        self.color = color

    def pick_it(self):
        print("Picked shoe")
    def remove_it(self):
        print("Removed it")

shoe1 = Shoe("Avunja","42","pitch")
shoe1.pick_it()
shoe2 = Shoe("Prada","32","green")
shoe2.pick_it()
shoe3 = Shoe("Puma","30","blue")
shoe1.remove_it()
shoe4 = Shoe("Air max","37","black")
shoe1.remove_it()

