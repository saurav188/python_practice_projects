#Given an integer n, calculate the square of 
#a number without using *, / and pow().

def get_ith_bit(num,i):
    temp=2**(i-1)
    temp=temp&num
    if temp==0:
        return 0
    else:
        return 1

def power(num):
    num=abs(num)
    result=0
    for i in range(32):
        ith_bit=get_ith_bit(num,i+1)
        if ith_bit==1:
            result+=num<<i
    return result

print(power(-20))

#        101
#        101
#       -----
#        101 
#       0000
#      10100
#     -------
#      11001=>25