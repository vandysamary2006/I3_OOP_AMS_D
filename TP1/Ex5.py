class LuckyNumberGame:
    """A game that returns the input number plus one."""
    def __init__(self, number):
        self.number = number

    def get_next_number(self):
        """Return the next number."""
        return self.number + 1

    def display_result(self):
        """Display the result."""
        print("The next number is :", self.get_next_number())

# Get input from the user
num = int(input("Enter an integer : "))

# Create an object and display the result
game = LuckyNumberGame(num)
game.display_result()
