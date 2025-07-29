alphabets='ABCDE'
dictionary={x:int(input("")) for x in alphabets}
print(dictionary)

for x in dictionary.keys():
    for y in dictionary.keys():
        if dictionary[x] > dictionary[y]:
           dictionary[x],dictionary[y]=dictionary[y],dictionary[x]

print(dictionary)

"""
WAY 1: use a list of values, sort and reupdate
 
WAY 2: use the idea of bubble sort, with 2 for loops, access the keys and now compare and swap

Update: dont use bubble sort , because key is may be a string
"""