# Count frequncy of each character

s="sirajuddin"
res={}
for char in s:
    if char in res:
        res[char]=res[char]+1
    else:
        res[char]=1
print(res)

"""
OUTPUT: {'s': 1, 'i': 2, 'r': 1, 'a': 1, 'j': 1, 'u': 1, 'd': 2, 'n': 1}

"""