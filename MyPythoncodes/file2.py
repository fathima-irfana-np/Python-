with open("irfanadet.txt",'r') as f:
    content=f.readlines()
    L=['#'+x for x in content]

with open("irfumol.txt",'w') as f1:
    f1.write(''.join(L)) 