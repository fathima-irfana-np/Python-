def fibo(num):
    count = 0
    LIST = []
    if num <= 1:
        return 1
    else:
        c = 0
        b = 1
        a = 0
        while c < num:  # Changed from c>num to c<num
            count += 1
            LIST.append(c)
            c = a + b
            a = b
            b = c
        print(LIST)
        return count  # Added return statement to return the count

n = int(input("Enter number: "))
print(fibo(n))
