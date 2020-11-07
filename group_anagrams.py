def groupAnagramWords(strs):
    anagrams=[]
    visited={}
    for i in range(len(strs)):
        if visited.get(i)==True:
            continue
        visited[i]=True
        temp=[strs[i]]
        temp_hash={letter:True for letter in strs[i]}
        for j in range(i+1,len(strs)):
            equal_lengths=len(strs[i])==len(strs[j])
            if not equal_lengths:
                continue
            is_anagram=True
            for letter in strs[j]:
                if temp_hash.get(letter)==None:
                    is_anagram=False
            if is_anagram:
                visited[j]=True
                temp.append(strs[j])
        anagrams.append(temp)
    return anagrams
print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]