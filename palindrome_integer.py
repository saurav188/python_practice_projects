import math

def is_palindrome(n):
    string_no=str(n)
    i=len(string_no)-1
    j=0
    while j<i:
        if string_no[j]!=string_no[i]:
            return False
        i-=1
        j+=1
    return True

print(is_palindrome(1234321))
# True
print(is_palindrome(1234322))
# False
