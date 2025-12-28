# Find the first non-repaeting character

s="sirajuddin"
def helper(s):
    for char in s:
        if s.count(char)==1:
            return char
    return 'No characters'
print(helper(s))

"""
OUTPUT: 

"""