your_first_n=int(input("Enter your first number: "))
your_second_n=int(input("Enter your second number: "))
print("Choose your action: +, -, *, /, ^")
your_choice=input("Enter your choice: ")
match your_choice:
    case "+":
        print(your_first_n+your_second_n)
    case "-":
        print(your_first_n-your_second_n)
    case "*":
        print(your_first_n*your_second_n)
    case "/":
        print(your_first_n/your_second_n)
    case "^":
        print(your_first_n**your_second_n)
    