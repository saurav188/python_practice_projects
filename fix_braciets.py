def fix_brackets(s):
    open=0
    count=0
    for i in range(len(s)):
        if s[i]=='(':
            open+=1
        elif s[i]==')':
            if open>0:
                open-=1
            else:
                count+=1
    return count+open
print(fix_brackets('())))(()()'))
# 4