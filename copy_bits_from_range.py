#Given two numbers x and y, and a range 
#[l, r] where 1 <= l, r <= 32. 
#The task is consider set bits of y 
#in range [l, r] and set these bits in x also.

def get_bits(num,i,j):
    bits=0
    for k in range(i-1,j):
        bits+=num&(2**k)
    return bits

def copy_bits(num1,num2,i,j):
    bit_set=get_bits(num2,i,j)
    return num1|bit_set

print(copy_bits(8,7,1,2))