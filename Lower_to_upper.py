# Convert string from lowercase to uppercase

s="jaris"
res=""
for char in s:
    res+=chr(ord(char)-32)
print(res)

"""
OUTPUT: JARIS
"""