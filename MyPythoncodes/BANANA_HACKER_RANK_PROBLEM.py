def print_substrings(string):
    for i in range(len(string)):
        for j in range(i+1, len(string) + 1):
            print(string[i:j])

s = input("Enter a string: ")
print_substrings(s)