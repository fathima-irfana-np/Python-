size=int(input('enter no.of module'))
keys1=[]
max=size*2

for i in range(1,max+1):
    keys1.append(i)
dictionary={}

for i in range(len(keys1)):
    dictionary.update({keys1[i]:0})
print(dictionary)
sum=0

for i in range(size*2):
    ques=input("enter ques no")
    if ques=='END':
        break
    else:
        ques=int(ques)
        dictionary[ques]=int(input("mark"))
        

for i in range(1,(len(keys1)),2):
    value1 = dictionary[i]
    value2 = dictionary[i+1]
    if (value1>=value2):
        sum+=value1
    else:
        sum+=value2

print(sum)
print(dictionary)




