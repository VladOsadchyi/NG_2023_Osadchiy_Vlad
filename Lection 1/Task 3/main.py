# Вибір напрямку переводу
your_choice = input("Choose what do you want (C->F or F->C) Print C (if 1) or F (if 2): ")
if your_choice == "C":
    celsius = float(input("Enter the temperature in degrees Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} deegrees Celsius = {fahrenheit} degrees Fahrenheit")
elif your_choice == "F":
    fahrenheit = float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} degrees Fahrenheit= {celsius} degrees Celsius")

