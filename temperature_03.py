"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

Rehashed version to support function calls
"""
def menu():
    user_choice = input("""C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
>>> """).upper()
    return user_choice


def fahrenheit_to_celsius(input_fahrenheit):
    converted_celsius = (input_fahrenheit - 32) / 9 * 5
    return converted_celsius


def celsius_to_fahrenheit(input_celsius):
    converted_fahrenheit = input_celsius * 9 / 5 + 32
    return converted_fahrenheit


choice = menu()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        converted_temperature = celsius_to_fahrenheit(celsius)
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        converted_temperature = fahrenheit_to_celsius(fahrenheit)
    else:
        print("Invalid option")
    print("Result: {:.2f}".format(converted_temperature))
    choice = menu()
print("Thank you")


"""
MENU = C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit
print(MENU)
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print("Result: {:.2f} F".format(fahrenheit))
    elif choice == "F":
        # TODO: Write this section to convert F to C and display the result
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        # Remove the "pass" statement when you are done. It's a placeholder.
        pass
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
"""