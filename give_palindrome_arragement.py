def find_palindrome(s):
    dict={}
    for letter in s:
        if dict.get(letter)==None:
            dict[letter]=1
        else:
            dict[letter]+=1
    mid_index=0
    palindrome=""
    for key in dict:
        if dict[key]>=2:
            while dict[key]>1:
                palindrome=key+palindrome+key
                dict[key]-=2
                mid_index+=1
        if dict[key]==1:
            palindrome=palindrome[:mid_index]+key+palindrome[:mid_index]
    return palindrome

print(find_palindrome('momom'))
# momom