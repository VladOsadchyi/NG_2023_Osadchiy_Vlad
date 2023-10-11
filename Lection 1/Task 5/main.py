your_list=input("Enter your list:  ").split()
count=0
for el in your_list:
    if el.isnumeric():
        count += 1
print("How many numbers do you have: ", count)