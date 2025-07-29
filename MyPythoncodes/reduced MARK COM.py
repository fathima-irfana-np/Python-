size=int(input('enter no.of module'))
dictionary={}
sum=0

# for i in range(1,size*2+1):
#     dictionary[i]=0

dictionary={i:0 for i in range(1,size*2+1)}
print(dictionary)


for i in range(1,size*2+1):
    ques=input("enter ques no")
    if ques=='END' or ques=='end':
        break
    else:
        ques=int(ques)
        dictionary[ques]=int(input("mark"))
        

print(dictionary)
for i in range(1,size*2+1,2):
    value1 = dictionary[i]
    value2 = dictionary[i+1]
    if (value1>=value2):
        sum+=value1
    else:
        sum+=value2

print(sum)