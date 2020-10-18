def look_say(n):
    if n==1:
        return "1"
    
    prev_sequence=look_say(n-1)

    num=None
    count=0
    temp=''
    for k in prev_sequence:
        if num==None:
            num=k
            count=1
        elif k==num:
                count+=1
        if k!=num:
            temp+=str(count)+num
            num=k
            count=1
    if num!=None:
        temp+=str(count)+num
    return temp

print(look_say(6))