#pancard_validation
#panncard format = AYRJD2345Q
import re
def pan_validation(number):
    format=r'^[A-Z]{5}[0-9]{4}[A-Z]{1}$'
    if len(number)!=10:
        return False
    elif(re.match(format,number)):
        return True
    else:
        return False
         
pannumber=input("enter a pan number")
result=pan_validation(pannumber)
if result is True:
    print('valid')
else:
    print('invalid')