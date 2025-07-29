size=int(input("enter size of list"))
L=[int(input("")) for i in range(size)]
L2=[x for x in L if x%2!=0]
dictionary={x:(x*x*x) for x in L2}
print(dictionary)

# [1,2,3,4,5]
# {1:1, 3:127}
# dictionary={x:(x*x*x) for x in L2}
# print(dictionary)
#list edka
#list ndaakki
#list ne odd number akkuka
#dictionary comprehension vazhi, dictionary ndaakuka





students = {
    "Alice": {"Math": 85, "English": 78, "Science": 92},
    "Bob": {"Math": 79, "English": 88, "Science": 84},
    "Charlie": {"Math": 91, "English": 92, "Science": 89}
}

l=students.items()
print(l)
score={}
for names,sub in l:
    score[names]=sum(sub.values())
print("The name and corresponding marks are",score)   
topper=max(score.keys())
high=max(score.values())
print(f"the high score is for {topper} with marks {high}")

##
##
##
##





students={
    "Alice":{"Math":85, "english":78 ,"Science":92 },
    "Bob":{"Math":79, "english":88 ,"Science":84 },
    "Charlie":{"Math":91, "english":92 ,"Science":89 },
}
dict1,dict2,dict3={},{},{}
sumA,sumB,sumC=0,0,0
dict1,dict2,dict3=students["Alice"],students["Bob"],students["Charlie"],
for x in dict1.values():
    sumA+=x
for x in dict2.values():
    sumB+=x  
for x in dict3.values():
    sumC+=x
    
print(f"charlie(Highest Score){ max(sumC,sumA,sumB) }" )

#key vech puthye dictionary edukkuka
#values eduth x il, enntt kootti koukkuka
#maximum venam print akkaan


# same dictionary values
# dict1={i:int(input("")) for i in "abc"}
# dict2={i:int(input("")) for i in "bcd"}
dict1={'a': 10, 'b': 20, 'c': 30}
dict2= {'b': 15, 'c': 25, 'd': 35}
print(dict1,dict2)

for x in dict1:
    for y in dict2:
        if x==y: # x and y are keys
            dict2[y]+=dict1[x]
print(dict1)
print(dict2)
dict4=dict1|dict2  #dict2 overrides dict1 when comes to union
print(dict4)


####
####
####



# dict1={i:int(input("")) for i in "abc"}
# dict2={i:int(input("")) for i in "bcd"}
dict1={'a': 10, 'b': 20, 'c': 30}
dict2= {'b': 15, 'c': 25, 'd': 35}
for x in dict1:
    for y in dict2:
        if x==y: # x and y are keys
            dict2[y]+=dict1[x]
dict1.update(dict2)
print(dict1)


people = {"Alice": 25, "Bob": 30, "Charlie": 25, "David": 30, "Eve": 35}
new_dict = {}
for name, age in people.items():
    if age not in new_dict:
        new_dict[age] = [] #value empty list edthu
    new_dict[age].append(name)

print(new_dict)



####
####
####
# Input: [("Alice", 85), ("Bob", 92), ("Charlie", 89), ("David", 95), ("Eve", 88)]
# Output: The top 3 students and their scores.
L=[("Alice", 85), ("Bob", 92), ("Charlie", 89), ("David", 95), ("Eve", 88)]
dictee=dict(L)
s=sorted(dictee.values())
max1=s[4]
max2=s[3]
max3=s[2]
for x in dictee.keys(): #x is key
    if dictee[x]==max1:
        print(f"the 1st topper is {x} with {max1} ")
    if dictee[x]==max2:
        print(f"the second topper is {x} with {max2} ")
    if dictee[x]==max3:
        print(f"the third topper is {x} with {max3} ")



####
####
####
# Input: [('a', 1), ('b', 2), ('a', 1), ('c', 3), ('a', 1)]
# Tuple to count: ('a', 1)
# Output: The count of the tuple ('a', 1).
L = [('a', 1), ('b', 2), ('a', 1), ('c', 3), ('a', 1), ('a', 1)]
m=input("enter a tuple")
count=0
for x in L:
    if x == eval(m):
        count+=1
print(count)



####
####
####
#Input: (1, 2, 2, 3, 4, 1, 5)
# Output: (1, 2, 3, 4, 5)
T= (1, 2, 2, 3, 4, 1, 5)
set_t=set(T)
str_t=str(set_t)
T=eval(str_t)
#tuple to set, set to string, str to tuple
print(T)

T = (1, 2, 2, 3, 4, 1, 5)  # Input tuple
T = tuple(set(T))          # Convert tuple to set (remove duplicates) and back to tuple
print(T)                   # Output: (1, 2, 3, 4, 5)




####
####
####
