size = int(input("size? "))
L = [[]]
n = [int(input("")) for i in range(size)]
for i in range(size):
    for j in range(len(L)):
        L.append(L[j] + [n[i]])

print(L)