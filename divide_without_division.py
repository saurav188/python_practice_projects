#Given a two integers say a and b. 
#Find the quotient after dividing 
#a by b without using multiplication, 
#division and mod operator.

def get_bits(num,i,j):
    bits=0
    for k in range(i-1,j):
        bits+=num&(2**k)
    return bits

def divide(a,b):
    quotient=0
    i=0
    temp1=0
    temp2=0
    sign=-1 if ((a<0) ^ (b<0)) else 1
    a=abs(a)
    b=abs(b)
    while a>=b:
        temp1=get_bits(a,33-i,32)
        temp2=b*(2**(32-i))
        if temp1>=temp2:
            a=a-temp2
            quotient+=2**(32-i)
        i+=1
    return sign*quotient
print(divide(250,-100))

#1010
#10
#10/1010\101 0 or 1 in decided by bits in range(32,32-1) where 1 keeps on decrease
#   10||     left shift decreases from 32
#   ----     
#    01|
#    00|
#   ----
#     10
#     10
#   ----
#      0