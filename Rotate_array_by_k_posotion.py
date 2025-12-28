# 8-> Rotate array by k positions

s=[1,2,3,4,5]
k=3
k=k%len(s)
res=s[len(s)-k:]+s[:len(s)-k]
print(res)

"""
OUTPUT: [3, 4, 5, 1, 2]

"""
