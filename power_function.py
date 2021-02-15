#The power function calculates x raised to the nth power. 
#If implemented in O(n) it would simply be a for loop 
#over n and multiply x n times. Instead implement this 
#power function in O(log n) time. You can assume that n 
#will be a non-negative integer.

def pow(x, n):
    if n==0:
        return 1
    elif n==1:
        return x
    elif n%2==0:
        return pow(x,n/2)*pow(x,n/2)
    else:
        return x*pow(x,(n-1)/2)*pow(x,(n-1)/2)


print(pow(4, 4))