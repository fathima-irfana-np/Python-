with open("lambda.py", "r") as f:
    f1 = f.readlines()
    for line in f1:

        words = line.strip().split()

        if len(words) > 0 and words[0] != " " and words[0:4] != "def ":
            print('#' + line, end='')  
        else:
            print(line, end='') 