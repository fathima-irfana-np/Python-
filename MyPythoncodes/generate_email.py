import re
def email(name):
    newline=''
    format=r'^[a-zA-Z]$'
    for x in name:
        if re.match(format,x):
            newline+=x
    return newline

string=input("enter your name")
number=input("enter your roll number")
result=email(string)
print(f"the email is {result}{number}@gmail.com")
