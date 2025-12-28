# Check if two strings are anagrams

s="siraj"
r="jaris"
def anagram(s,r):
    for char in s:
        if char not in r:
            return 'Not Anagram'
        return 'Anagram'
print(anagram(s,r))

"""
OUTPUT: Anagram

"""