def find_anagrams(s, t):
    length_of_anagrams=len(t)
    letters={}
    result=[]
    is_anagram=False
    for letter in t:
        letters[letter]=True
    for i in range(len(s)):
        if letters.get(s[i])!=None:
            if len(s)-i<length_of_anagrams:
                continue
            temp=s[i:i+length_of_anagrams]
            is_anagram=True
            for j in temp:
                if letters.get(j)==None:
                    is_anagram=False
                    break
            if is_anagram:
                result.append(i)
    return result

print(find_anagrams('acdbacdacb', 'abc'))
# [3, 7]