# import math
# print(dir(str))
# help(str.maketrans)
# # help(math.sqrt)
rep=str.maketrans("apple","anime")
print(rep)

translation_table = str.maketrans('aN', 'zP')
print("irfana NP".translate(translation_table))

translation_tablle=str.maketrans('a','X')
print("irfananp".translate(translation_tablle))

translation = str.maketrans('   ', 'abc')
print("ab    cdef".translate(translation)) 

# Remove 'a', 'b', and 'c'
translation_tabe = str.maketrans('', '', 'abc')
print("abcdef".translate(translation_tabe)) 