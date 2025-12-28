# Convert string from uppercase into lowercase

s="JARIS"
res=""
for char in s:
    res+=chr(ord(char)+32)
print(res)

"""
OUTPUT: jaris

"""