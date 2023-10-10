# Введення трьох чисел у масив
user_input = input("Enter three numbers separated by spaces: ")
list_with_numbers = [float(number) for number in user_input.split()]
if len(list_with_numbers ) != 3:
    print("Please enter exactly three numbers separated by spaces.")
else:
    your_first_n, your_second_n, your_third_n = list_with_numbers 
    Dis = your_second_n**2 - (4 * your_first_n * your_third_n)
    print("Your D= ", Dis)
    if Dis > 0:
        x1 = (-your_second_n + Dis**0.5) / (2 * your_first_n)
        x2 = (-your_second_n - Dis**0.5) / (2 * your_first_n)
        print("Your x1= ", x1, '\n' "Your x2= ", x2)
    elif Dis == 0:
        x1 = (-your_second_n + Dis**0.5) / (2 * your_first_n)
        print("Your x1= ", x1)
    else:
        print('There are no D')
