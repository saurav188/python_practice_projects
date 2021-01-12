def to_bits(n):
    return str(bin(n))[2:]

def get_bit(num,index):
    temp=(2**index)
    if num&temp==0:
        return 0
    else:
        return 1

def reverse_num_bits(num):
    result=0
    for i in range(32):
        current_bit=get_bit(num,i)
        if current_bit==1:
            result+=(2**(31-i))
    return result

print(to_bits(1234))
# 10011010010
print(reverse_num_bits(1234))
# 1260388352
print(to_bits(reverse_num_bits(1234)))
# 1001011001000000000000000000000