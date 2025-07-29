list1 = [1,2,3,4,5]
list2 = [1, 2, 3,8,9]

list14=[x for x in list1 if x in list2]
list13=[x for x in list1 if x not in list2 ]
list13=list2+list13

print(list14)#intersection
print(list13)#union
