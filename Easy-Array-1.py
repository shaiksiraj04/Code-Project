# 1 -> Find the largest and smallest element in an array

s=[1,5,7,-10]
largest=float('-inf')
smallest=float('inf')
for num in s:
    if num>largest:
        largest=num 
    if num<smallest:
        smallest=num 
print(largest,smallest)

"""
OUTPUT : 7 -10

"""