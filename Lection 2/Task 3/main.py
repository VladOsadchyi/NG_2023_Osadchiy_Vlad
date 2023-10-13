your_number=int(input("Enter your number: "))
print("Number   | Dividers|   Simple?")
for i in range(1, your_number + 1):
    divisors = [str(j) for j in range(1, i + 1) if i % j == 0]
    prime = "Yes" if all(i % j != 0 for j in range(2, i)) else "No"
    print(f"{i} | {', '.join(divisors)} | {prime}")
prime_numbers = [i for i in range(1, your_number + 1) if all(i % j != 0 for j in range(2, i)) and i > 1]
print("-"*30)
print("\nSimple numbers:", prime_numbers)