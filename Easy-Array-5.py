# 5-> Move all zeros to the end

s=[1,10,2,4,0,7,8,11,0,12]
res=[]
for num in s:
    if num!=0:
        res.append(num)
print(res+[0]*(len(s)-len(res)))

"""
OUTPUT: [1, 10, 2, 4, 7, 8, 11, 12, 0, 0]

"""