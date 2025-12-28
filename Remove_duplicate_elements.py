# Remove duplicate elements in string

s="sirajuddin"
res=""
i=0
j=i+1
for char in s:
    if char not in res:
        res=res+char
print(res)

"""
OUTPUT: sirajudn

"""