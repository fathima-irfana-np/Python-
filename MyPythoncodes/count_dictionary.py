#we are going to count the same number of occurances in a dictionary

alphabets='ABCDE'
dict1={x:int(input("")) for x in alphabets}
print(dict1)

L=[x for x in dict1.values()]
L2=[]
for x in L:
    if x not in L2:
        L2.append(x)

for x in L2:
    count=0
    for y in dict1.values():
        if x==y:
            count+=1
    print(f"{x} occured {count} times")


# for x in L2:
#     count=L.count(x)
#     print(f"{x} occured {count} times")