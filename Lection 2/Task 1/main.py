your_list=input("Enter your symbols: ").split()
final_list=[]
for el in your_list:
    if your_list.count(el)==1:
        final_list.append(el)
print("Your unique elements:", final_list)