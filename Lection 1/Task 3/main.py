your_choice = input("Print C - if you want convert celsius to fahrenheit, or F if vice versa: ")
if your_choice == "C":
    your_number = float(input("Enter the temperature in degrees Celsius: "))
    fahrenheit = (your_number * 9/5) + 32
    print(f"{your_number} deegrees Celsius = {fahrenheit} degrees Fahrenheit")
elif your_choice == "F":
    your_number= float(input("Enter the temperature in degrees Fahrenheit: "))
    celsius = (your_number - 32) * 5/9
    print(f"{your_number} degrees Fahrenheit= {celsius} degrees Celsius")
else:
    print("Sorry!You write not correct letter")

