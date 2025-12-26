# 13-> Find all even and odd numbers separately

s=[1,34,56,23,56,0,1,2,7]
even=[]
odd=[]
for num in s:
    if num%2==0:
        even.append(num)
    else:
        odd.append(num)
print("even",even)
print("odd",odd)

"""
OUTPUT: even [34, 56, 56, 0, 2]
        odd [1, 23, 1, 7]

"""