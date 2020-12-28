KAPREKAR_CONSTANT = 6174

def num_kaprekar_iterations(n):
    count=0
    while n!=KAPREKAR_CONSTANT:
        each_no=[int(each) for each in str(n)]
        each_no.sort()
        ascending=0
        descending=0
        for i in range(len(each_no)):
            descending+=(each_no[i]*(10**i))
            ascending+=(each_no[len(each_no)-i-1]*(10**i))
        while len(str(descending))<4:
            descending=descending*10
        n=descending-ascending
        count+=1
    return count
        
print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)