f = open("irf1.py", "r")
lines=f.readlines()
print(lines)
newlines=[]
for line in lines:
        if  line[0] != " " and line[0:4]!='def ' :
                newlines.append('#'+line)
        else:
               newlines.append(line)
print(newlines)
new=''.join(str(''.join(newlines)))
f = open("irf16.out", "x")
f.write(new)
f.close()