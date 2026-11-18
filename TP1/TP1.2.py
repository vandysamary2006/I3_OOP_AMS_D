class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def perimeter(self):
        return 2 * (self.width + self.length)

    def area(self):
        return self.width * self.length

    def display_result(self):
        print(f"Perimeter: {self.perimeter()}")
        print(f"Area: {self.area()}")

while True:
    try:
        width = float(input("Enter width (-1 to exit): "))

        if width == -1:
            print("Program ended.")
            print("")
            break

        elif width <= 0:
            print("Invalid input! Width can not 0 or negative number!")

        else:
            while True:
                try:
                    length = float(input("Enter length: "))

                    if length <= 0:
                        print("Invalid input! Length can not 0 or negative number!")
                        continue

                    elif length < width:
                        print("The length can not smaller than width.")
                        continue

                    else:
                        rectangle = Rectangle(width, length).display_result()
                        print()
                        break
                except ValueError:
                        print("INVALID: Please enter a numeric value.")

    except ValueError:
        print("INVALID: Please enter a numeric value.")
