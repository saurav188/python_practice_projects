#Given an expression (as a list) in reverse polish notation, 
#evaluate the expression. Reverse polish notation is where 
#the numbers come before the operand. Note that there can 
#be the 4 operands '+', '-', '*', '/'. 
#You can also assume the expression will be well formed.

#Example
#Input: [1, 2, 3, '+', 2, '*', '-']
#Output: -9
#The equivalent expression of the 
#above reverse polish notation would be (1 - ((2 + 3) * 2)).

def reverse_polish_notation(expr):
    if len(expr)==1:
        return expr[0]
    temp='('+str(expr[0])+str(expr[-1])+"("+str(reverse_polish_notation(expr[1:-1]))+")"+")"
    return eval(temp)

# 1 - (2 + 3) * 2
print(reverse_polish_notation([1, 2, 3, 2, '+', '*', '-']))
# -9