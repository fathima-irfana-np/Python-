n=int(input(""))
k=1
for i in range(1,n+1):#NO.of rows
    for j in range (i):#each row lines
        if i%2!=0:
            if (j+1)%2!=0:
                print((chr(96+k)).upper(),end="")
            else:
                print(chr(96+k),end="")
        else:
            if (j+1)%2!=0:
                print(chr(96+k),end="")
            else:
                print((chr(96+k)).upper(),end="")                
        k+=1
    print("\n")


# Z=6
# count = 0
# for i in range(1, Z+1):
#     for j in range(i):
#         if i % 2!=0:
#             if (j+1)% 2 != 0:
#                 print(chr(65+ count), end= "")
#             else:
#                 print(chr(97+ count), end="")
#         else:
#             if (j+1)% 2==0:
#                 print(chr(65+ count), end= "")
#             else:
#                 print(chr(97+ count), end="")
#         count+=1
#     print()
