def longest_substring_with_k_distinct_characters(s, k):
    def getnextletter(string,start):
        for i in range(start,len(string)):
            if string[i]!=string[i+1]:
                return i+1
    pointer1=0
    pointer2=None
    no_letters=1
    for i in range(1,len(s)):
        pointer2=i
        if no_letters<k:
            if s[pointer2-1]!=s[pointer2]:
                no_letters+=1
        else:
            if s[pointer2-1]!=s[pointer2]:
                pointer1=getnextletter(s,pointer1)
    return s[pointer1:pointer2+1]



print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)

#2 pointer for start and end of substring  
#pointer2 increses with iteration
#if no_letters<3 => letters change no_letter+=1
#else            => pointer1 change to next letter from start 