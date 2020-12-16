# the array as input parameter and returns a list of 
#two numbers which occur exactly once in the array.
def get_non_repeating(array):
    xor_all=0
    for each in array:
        xor_all^=each
    right_most_bit=xor_all&(~(xor_all-1))
    num1=0
    num2=0
    for each in array:
        if right_most_bit&each>0:
            num1^=each
        else:
            num2^=each
    return [num1,num2]

print(get_non_repeating([1 ,2 ,3 ,2 ,1 ,4,3,14]))
#4,14