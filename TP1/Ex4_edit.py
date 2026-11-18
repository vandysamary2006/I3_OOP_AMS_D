class HundredsCounter:
    def __init__(self, number):
        self.number = number

    def count_hundreds(self):
        return self.number // 100


while True:
    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Error: Number must be non-negative.")
        else:
            print("Complete hundreds:", HundredsCounter(number).count_hundreds())

    except ValueError:
        print("Error: Please enter a valid integer.")

