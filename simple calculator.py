def evalu(expression):
    if len(expression)==1 or len(expression)==0:
        return expression
    for i in range(len(expression)-1):
        break_this=False
        if expression[i]=='(':
            for j in range(len(expression)-1,0,-1):
                if expression[j]==')':
                    if i>0 and j<len(expression):
                        expression=expression[0:i-1]+eval(expression[i+1:j-1])+expression[j+1:len(expression)]
                    break_this=True
                    break
        if break_this:
            break
    temp=''
    for each in expression:
        if each!=' ':
            temp+=each
    expression=temp
    if expression[0] in ['0','1','2','3','4','5','6','7','8','9']:
        if expression[1]=='+':
            return str(int(expression[0])+int(expression[2]))
        elif expression[1]=='-':
            return str(int(expression[0])-int(expression[2]))
    return expression
print(eval('4 + (2+( 2 - 1-2 ) )'))
# -4
#(1+(1+(1+1)))