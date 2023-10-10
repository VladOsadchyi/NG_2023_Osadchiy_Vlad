your_list=input("Enter your symbols: ").split()
for el in your_list:
    if your_list.count(el)==1:
       print("Your unique element:", el)