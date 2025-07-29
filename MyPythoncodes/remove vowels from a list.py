#remove vowels from a string
string=input("enter a string")
vowels='aeiouAEIOU'
newline=''
for i in range(len(string)):
    if string[i] not in vowels:
        newline+=string[i]
print(newline)
