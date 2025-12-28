s="MADAM"
def palindrome(s):
    res=""
    for i in range(-1,-6,-1):
        res=res+s[i]
    print(res)
    if res==s:
        return 'Palindrome'
    else:
        return 'Not Palindrome'
print(palindrome(s))

"""
OUTPUT: MADAM
        Palindrome

"""