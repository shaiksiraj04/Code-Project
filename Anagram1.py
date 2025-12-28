# Check if the two strings are anagram 

s="siraj"
r="jaris"
def anagram(s,r):
    if len(s)!=len(r):
        return 'Not Anagaram'
    for char in s:
        if char not in s:
            return 'Not Anagaram'
        return 'Anagram'
print(anagram(s,r))

"""
OUPTUT: Anagram

"""