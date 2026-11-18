class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price

class EBook(Book):
    pass

"""Summarize principles of OOP"""
#OOP has four main principles: Encapsulation, Abstraction, Inheritance, and Polymorphism.
#1.Encapsulation is the class private attributes and methods, which can protect data from direct external modification.
#2.Abstraction is the process of hiding complex implementation details and showing only essential features to the user. 
#3.Inheritance is the process in OOP that a child class inherits properties(attributes) and methods from a parent class and can also promote code reuse.
#4.Polymorphism is the same method name can behave differently depending on the object.