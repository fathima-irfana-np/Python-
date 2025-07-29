#we are craeting an dictionary and then we will sort it 
#values list lekk edthtt sort cheythu

alphabets='ABCDE'
dictionary={x:int(input("")) for x in alphabets}
print(dictionary)

list1=[x for x in dictionary.values()]
list1.sort()

print("Printing In Ascending Order:\n")
i=0
for key_x in dictionary:
    dictionary[key_x]=list1[i]
    i+=1
print(dictionary)

print("Printing In Descending Order:\n")
i=len(list1)-1
for key_x in dictionary:
    dictionary[key_x]=list1[i]
    i-=1
print(dictionary)

"""
use a bubble sort on the list if you want to sort a list
ee method values list kk edthen,ennt thirich update akki, ithallathe dictionaries nn neritt cheyyavo? maatamo???

"""
