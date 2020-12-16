# find position of the only set bit.
def set_bit_position(num):
    if num==1:
        return 1
    position=0
    while True:
        position+=1
        if (2**(position-1))==num:
            return position

print(set_bit_position(64))
#7