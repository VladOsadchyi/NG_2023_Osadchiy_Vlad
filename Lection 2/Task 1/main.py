your_list = input("Enter your symbols: ").split()
print("Your unique elements:", [el for el in your_list if your_list.count(el) == 1])

