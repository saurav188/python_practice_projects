#Given a 32-bit integer, swap the 1st and 2nd bit, 
#3rd and 4th bit, up til the 31st and 32nd bit.

def get_bit(num,i):
    temp=2**i
    if temp&num==0:
        return 0
    else:
        return 1

def swap_bits(num):
    result=0
    bit1=0
    bit2=0
    for i in range(0,32,2):
        bit1=get_bit(num,i)
        bit2=get_bit(num,i+1)
        if bit2==1:
            result+=2**i
        if bit1==1:
            result+=2**(1+i)
    return result

print(f"0b{swap_bits(0b10101010101010101010101010101010):032b}")
# 0b01010101010101010101010101010101