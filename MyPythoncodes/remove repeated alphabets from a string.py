def remove_repetition(string):
    newline=''
    for x in string:
        if x not in newline:
            newline+=x
    return newline

s=input("enter a string")
print(remove_repetition(s))