#Problem: Check if a given string of parentheses is balanced. The string contains (), {}, [].

inp=input("enter")
for i in range(len(inp)):
    if x in "{([" and inp[i] in "]})":
        print("valid")
    else:
        print("not valid")
        

