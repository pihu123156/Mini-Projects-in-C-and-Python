def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def inches_to_cm(inch):
    return inch * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def meters_to_feet(m):
    return m * 3.28084

def feet_to_meters(ft):
    return ft / 3.28084

def main():
    while True:
        print("\n📐 Temperature & Unit Converter")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Inches to Centimeters")
        print("6. Centimeters to Inches")
        print("7. Meters to Feet")
        print("8. Feet to Meters")
        print("0. Exit")

        choice = input("Choose an option (0-8): ")

        if choice == '0':
            print(" Goodbye!")
            break

        try:
            value = float(input("Enter value to convert: "))
        except ValueError:
            print(" Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(f"🌡️ Result: {celsius_to_fahrenheit(value):.2f} °F")
        elif choice == '2':
            print(f"🌡️ Result: {fahrenheit_to_celsius(value):.2f} °C")
        elif choice == '3':
            print(f"🌡️ Result: {celsius_to_kelvin(value):.2f} K")
        elif choice == '4':
            print(f"🌡️ Result: {kelvin_to_celsius(value):.2f} °C")
        elif choice == '5':
            print(f"📏 Result: {inches_to_cm(value):.2f} cm")
        elif choice == '6':
            print(f"📏 Result: {cm_to_inches(value):.2f} in")
        elif choice == '7':
            print(f"📏 Result: {meters_to_feet(value):.2f} ft")
        elif choice == '8':
            print(f"📏 Result: {feet_to_meters(value):.2f} m")
        else:
            print(" Invalid choice. Try again.")


main()
