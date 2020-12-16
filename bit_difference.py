#You are given two numbers A and B. 
#The task is to count the number of 
#bits needed to be flipped to convert A to B.
def bit_difference(num1,num2):
    and_value=num1^num2
    count=0
    while and_value!=0:
        and_value=and_value&(and_value-1)
        count+=1
    return count

print(bit_difference(20,25))