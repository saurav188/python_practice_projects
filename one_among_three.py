#Given a list of integer where every element appears
# three time except for one, find that unique one in O(1) space.
def get_ith_bit(num,i):
    mask=2**i
    temp=num&mask
    if temp==0:
        return 0
    else:
        return 1
def find_odd(array):
    bits=[]
    for k in range(32):
        temp1=0
        for i in range(len(array)):
            temp1+=get_ith_bit(array[i],k)
        bits.insert(0,temp1%3)
    temp1=0
    i=0
    for k in range(len(bits)-1,-1,-1):
        temp1+=(int(bits[k])*(2**i))
        i+=1
    return temp1

print(find_odd([1, 1, 2, 4, 2, 6, 4, 2, 1, 4]))