thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

m=thisdict.keys()
print(m) 
print(thisdict)

mydict={i:0 for i in range(11)}
print(mydict)

dictt={}
for i in range(11):
	dictt[i]="hello"
print(dictt)

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
dic4 = {}

for z in (dic1, dic2, dic3):
    dic4.update(z)
print(dic4) 

# key(), values(), items() =tuple il avum verika
# pop("key"),popitem() 
# copy() dictionary to another one
# dict.fromkeys(keys[as anything],0)