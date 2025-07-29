num = int(input("Enter a number: "))
if(num is 0):
    print("zero")
elif (abs(num) - num) is 0:
    print("Positive")
else:
    print("Negative")

#method 2
num = int(input("Enter a number: "))
if (num >> 31) :#31 << bit
    print("Negative")
else:
    print("Positive or Zero")