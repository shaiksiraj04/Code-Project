# 2-> Reverse an array in-place

s=[1,5,8,6,10,-1]
i=0
j=4
while i<j:
    s[i],s[j]=s[j],s[i]
    i=i+1
    j=j-1
print(s)

"""
OUTPUT: [10, 6, 8, 5, 1, -1]

"""