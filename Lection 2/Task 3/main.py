your_number=int(input("Enter your number: "))
print("Number   | Dividers|   Simple?")
for el in range(1, your_number + 1):
    divisors = [str(div) for div in range(1, el + 1) if el % div == 0]
    prime = "Yes" if all(el % div != 0 for div in range(2, el)) else "No"
    print(f"{el} | {', '.join(divisors)} | {prime}")
prime_numbers = [el for el in range(1, your_number + 1) if all(el % div != 0 for div in range(2, el)) and el > 1]
print("-"*30)
print("\nSimple numbers:", prime_numbers)