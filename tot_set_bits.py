#Find the total count of set bits 
#for all numbers from 1 to N(both inclusive).
def tot_set_bits(num):
    tot_count=0
    for i in range(1,num+1):
        count=0
        temp=i
        while temp!=0:
            temp=temp&(temp-1)
            count+=1
        tot_count+=count
    return tot_count
print(tot_set_bits(17))