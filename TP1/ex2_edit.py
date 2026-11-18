class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def display_result(self):
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")


while True:
    try:
        width = float(input("Enter width (-1 to exit): "))

        if width == -1:
            print("Program ended.")
            break

        height = float(input("Enter height: "))

        if width < 0 or height < 0:
            print("INVALID: Dimensions cannot be negative.")
            continue

        rectangle = Rectangle(width, height).display_result()
        print()

    except ValueError:
        print("INVALID: Please enter a numeric value.")

