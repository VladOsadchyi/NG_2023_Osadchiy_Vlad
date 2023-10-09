input_your_string = input("Enter your string: ")
vowels = "AEIOUaeiou"  
vowel_string =[]
for el in input_your_string:
    if el in vowels:
        vowel_string.append(el)
print(vowel_string)