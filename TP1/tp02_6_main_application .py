from tp02_1_greeting import Greeting
from tp02_2_rectangle import Rectangle
from tp02_3_equation import EquationCalculator
from tp02_4_hundreds_counter import HundredsCounter
from tp02_5_lucky_number import LuckyNumberGame

EXIT_CHOICE = "0"
MENU_TITLE = "=========== TP02 Python OOP =========="
MENU_OPTIONS = {
    "1": "Greeting",
    "2": "Rectangle",
    "3": "Equation Calculator",
    "4": "Hundreds Counter",
    "5": "Cheater Game",
    EXIT_CHOICE: "Exit",
}


class InvalidInputError(Exception):
    """Raised when the user enters data the program cannot accept."""


# ---------- input helpers ----------
def read_number(prompt, number_type=float):
    """Read a number of the given type, or raise InvalidInputError."""
    try:
        return number_type(input(prompt))
    except ValueError:
        raise InvalidInputError("Please enter a valid number.")


def read_non_negative_number(prompt, number_type=float):
    """Read a number that must not be negative."""
    value = read_number(prompt, number_type)
    if value < 0:
        raise InvalidInputError("The number cannot be negative.")
    return value


# ---------- one function per menu option ----------
def run_greeting():
    name = input("Enter your name: ")
    print(Greeting(name).get_greeting())


def run_rectangle():
    width = read_non_negative_number("Enter the width: ")
    height = read_non_negative_number("Enter the height: ")
    rectangle = Rectangle(width, height)
    print(f"Perimeter: {rectangle.calculate_perimeter()}")
    print(f"Area: {rectangle.calculate_area()}")


def run_equation_calculator():
    y = read_number("Enter y: ")
    z = read_number("Enter z: ")
    print(f"Calculated x: {EquationCalculator(y, z).calculate_x()}")


def run_hundreds_counter():
    number = read_non_negative_number("Enter a non-negative integer: ", int)
    print(f"Complete hundreds: {HundredsCounter(number).get_complete_hundreds()}")


def run_cheater_game():
    number = read_number("Enter an integer: ", int)
    print(f"Result (number plus one): {LuckyNumberGame(number).get_next_number()}")

MENU_ACTIONS = {
    "1": run_greeting,
    "2": run_rectangle,
    "3": run_equation_calculator,
    "4": run_hundreds_counter,
    "5": run_cheater_game,
}


# ---------- menu ----------
def show_menu():
    print(f"\n{MENU_TITLE}")
    for choice, label in MENU_OPTIONS.items():
        print(f"{choice}. {label}")


def run_choice(choice):
    """Run the selected option and show a message if something goes wrong."""
    action = MENU_ACTIONS.get(choice)
    if action is None:
        print("Invalid option! Please select a number from 0 to 5.")
        return
    try:
        action()
    except InvalidInputError as error:
        print(f"Invalid input! {error}")
    except ZeroDivisionError:
        print("Invalid input! z cannot be zero.")


def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()
        if choice == EXIT_CHOICE:
            print("Thank you for using the program. Goodbye!")
            break
        run_choice(choice)


if __name__ == "__main__":
    main()