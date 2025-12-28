# Find the first non-repeating character

s="sirajuddin"
flag=True
for char in s:
    if s.count(char)==1:
        print(char)
        flag=False
        break
if flag:
    print("No characters")

"""
OUTPUT: s

"""