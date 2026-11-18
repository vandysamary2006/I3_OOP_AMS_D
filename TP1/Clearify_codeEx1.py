class Greeting:
"""A class that greets a user."""

    def init(self, name):
     """Initialize the user's name."""
        self.name = name

    def say_hello(self):
     """Display a greeting message."""
        print(f"Hello, {self.name}!")

name = input("Enter your name: ")
greeting = Greeting(name)
greeting.say_hello()