class Solution:
    def reverse(self, x):
        in_range=x>=(-2**31) and x<=((2**31)-1)
        if not in_range:
            return 0
        string_no=str(x)
        reversed_string=''
        for i in range(len(string_no)-1,-1,-1):
            reversed_string+=string_no[i]
        return int(reversed_string)

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0

#Write a function that reverses the digits a 32-bit signed integer, x.
#Assume that the environment can only store integers within the 32-bit 
#signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when 
#the reversed integer overflows.