def fact(n):
    temp=1
    for i in range(1,n+1):
        temp=temp*i
    return temp
def correct_order(current_string):
    for i in range(1,len(current_string)):
        if current_string[i-1]==current_string[i]:
            return False
    return True
def rearrangeString(s):
    indexes=[i for i in range(len(s))]
    for each in range(fact(len(s))):
        current_string=''
        for index in indexes:
            current_string+=s[index]
        if correct_order(current_string):
            return current_string
        temp=0
        for i in range(len(s)-1,-1,-1):
            if indexes[i]>indexes[i-1]:
                temp=i-1
                break
        y=0
        for j in range(len(s)):
            if indexes[temp]<indexes[j]:
                y=j
        indexes[temp],indexes[y]=indexes[y],indexes[temp]
        indexes=indexes[:temp+1]+indexes[temp+1:][::-1]
print(rearrangeString('abbccc'))
# cbcabc