# L1=[1,2,4,1,3,4]
# L2=[]
# for x in L1:
#     if x not in L2:
#         L2.append(x)
# print(L2)




# map() example: applying a lambda to double each number in the list
numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))  # Output: [2, 4, 6, 8]
# filter() example: applying a lambda to keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))  # Output: [2, 4]
print(even_numbers)
print(doubled)
even_number = list(map(lambda x: x % 2 == 0,even_numbers )) 
print(even_number)





# from functools import reduce
# numbers = [1, 2, 3, 4]
# total = reduce(lambda x, y: x + y, numbers)  # Output: 10
# print(total)


strings = ["apple", "", "banana", None, "cherry"]
# Use filter to remove empty strings and None
non_empty_strings = list(filter(lambda x: x, strings))
print(non_empty_strings)