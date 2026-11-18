class EquationCalculator:
    def __init__(self, y, z):
        self.y = y
        self.z = z

    def calculate_x(self):
        # Validate inputs
        if self.y == 0:
            raise ValueError("y must not be 0.")
        if self.z == 0:
            raise ValueError("z must not be 0.")
        if self.y + self.z == 0:
            raise ValueError("y + z must not be 0.")

        #return value x = yz / (y + z)
        return (self.y * self.z) / (self.y + self.z)

    def display_result(self):
        #Show result
        try:
            x = self.calculate_x()
            print(f"x = {x}")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    #get user input
    try:
        y = float(input("Enter y: "))
        z = float(input("Enter z: "))
    except ValueError:
        print("Error: please enter valid numbers.")
        return

    calculator = EquationCalculator(y, z)
    calculator.display_result()

if __name__ == "__main__":
    main()
