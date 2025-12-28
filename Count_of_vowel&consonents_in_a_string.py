s="StudyIng" 
vowel_count=0
consonent_count=0
for char in s:
    if char in "aeiouAEIOU":
        vowel_count+=1
    else:
        consonent_count+=1
print("vowels :",vowel_count)
print("consonets :",consonent_count)
