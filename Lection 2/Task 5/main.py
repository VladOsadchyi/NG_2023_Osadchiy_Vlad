your_list=(input("Enter your message: "))
key=int(input("Enter your key: "))
result=''
main_alfavit='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in your_list:
    pos=main_alfavit.find(i)
    newpos=pos+key
    if i in main_alfavit:
        result+=main_alfavit[newpos]
    else:
        result+=i
print("-"*30, '\n', result)
