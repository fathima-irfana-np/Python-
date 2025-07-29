thistuple = ("apple", "banana", "cherry","orange")
print(thistuple[2])



(oi,bi,*ci) = thistuple

print(bi)
print(ci)
thistuple=str(thistuple)

A={1,2}
B={5,6,2}

A.update(B)
print(A)

C=A.union(B)
print(C)


C=A.symmetric_difference(B)
print(C)

