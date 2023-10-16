your_file=input("Enter the name of your file or the way to it: ")
count_of_char={}
with open(your_file, 'r') as file:
    for line in file:
        line=line.strip()
        for char in line:
            if char in count_of_char:
                count_of_char[char]+=1
            else:
                count_of_char[char]=1
print(count_of_char)
                
            