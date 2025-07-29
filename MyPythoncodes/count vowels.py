def count_vowels(List1):
    vowels='aeiouAEIOU'
    count=0
    for word in List1:
        for y in word:
            if y in vowels:
                count+=1
    return count

size=int(input("enter size of list"))
List=[input("") for i in range(size)]
result=count_vowels(List)
# print(f"the count is {result}")
print("the count is",result)