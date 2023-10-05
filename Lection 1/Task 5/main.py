your_first_n=float(input("Enter your first number of equation: "))
your_second_n=float(input("Enter your second number of equation: "))
your_third_n=float(input("Enter your first number of equation: "))
Dis=your_second_n**2 - (4*your_first_n*your_third_n)
print("Yor D= ", Dis)
if Dis>0:
    x1=(-your_second_n+Dis**0.5)/(2*your_first_n)
    x2=(-your_second_n-Dis**0.5)/(2*your_first_n)
    print("Your x1= ",x1,'\n'"Your x2= ",x2)
else:
    print('There are no D')