def decodeString(s):
    contains_no=False
    no_index=False
    numbers=['0','1','2','3','4','5','6','7','8','9']
    for i in range(len(s)):
        if s[i] in numbers:
            contains_no=True
            no_index=i
            break
    if not contains_no:
        return s
    start=no_index+2
    end=start
    for j in range(len(s)-1,start-1,-1):
        if s[j]==']':
            end=j-1
            break
    result=decodeString(s[start:end+1])
    temp=result
    for i in range(int(s[no_index])-1):
        result+=temp
    result=s[:no_index]+result+s[end+2:]
    return result
print(decodeString('2[a2[b]c]'))
# abbcabbc