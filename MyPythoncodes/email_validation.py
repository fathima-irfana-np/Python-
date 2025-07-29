import re
def email_valid(string):
    if not string:
        print("invalid entry, try again")
        return False
    else:
        pattern=r'^[0-9a-zA-Z._+%-]+@[0-9a-zA-Z.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern,string):
            return True
        else:
            return False

email=input("enter your email")
result=email_valid(email)
if(result is True):
    print("valid")
else:
    print("invalid")