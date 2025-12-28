# Check if string is a palindrome
s="MADAM"
def check_palindrome(s):
    i=0
    j=len(s)-1
    while i<j:
        if s[i]!=s[j]:
            return 'Not Palindrome'
        i+=1
        j-=1
    return 'Palindrome'
print(check_palindrome(s))

"""
OUTPUT: Palindrome

"""