string=input("")
newline=''
for x in string:
    if x=='_':
        m=input("enter")
        newline+=m
    else:
        newline+=x
num=int(newline)
print(num)
if(num%11==0):
    print("yes")
else:
    print("noooo")


string=input("")
for x in string:
    if x=='_':
        string=string.replace(x,input())
print(string)