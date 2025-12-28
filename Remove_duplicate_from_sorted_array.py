# 4-> Remove duplicates from a sorted array

s=[1,2,3,5,6,6,7,8,8]
res=[]
for num in s:
    if num not in res:
        res.append(num)
print(res)

"""
OUTPUT: [1, 2, 3, 5, 6, 7, 8]

"""
