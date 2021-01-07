def has_character_map(str1, str2):
    dict={}
    i=0
    while i<len(str1):
        if dict.get(str1[i])==None:
            dict[str1[i]]=str2[i]
        else:
            if dict[str1[i]]!=str2[i]:
                return False
        i+=1
    return True

print(has_character_map('abc', 'def'))
# True
print(has_character_map('aac', 'def'))
# False