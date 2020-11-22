class Solution():
    def romanToInt(self, s):
        singles={
            'I'     :1,
            'V'     :5,
            'X'     :10,
            'L'     :50,
            'C'     :100,
            'D'     :500,
            'M'     :1000
        }
        doubles={
            'IV'    :4,
            'IX'    :9, 
            'XL'    :40,
            'XC'    :90,
            'CD'    :400,
            'CM'    :900
        }
        result=0
        i=0
        while i<len(s):
            if i==len(s)-1:
                result+=singles[s[i]]
                i+=1
                continue
            #checking for 4,9,40,90,400,900
            if s[i] in ['I','X','C']:
                is_4_40_400_900 = (s[i+1] in ['V','L','D','M'])
                is_9            = (s[i]=='I' and s[i+1]=='X')
                is_90           = (s[i]=='X' and s[i+1]=='C')
                if is_4_40_400_900 or is_9 or is_90:
                    result+=doubles[s[i:i+2]]
                    i+=2
                    continue
            result+=singles[s[i]]
            i+=1
        return result
    
n = 'MCMX'
print(Solution().romanToInt(n))
# 1910

""" Roman numerals are based on the following symbols:
I     1
IV    4
V     5
IX    9 
X     10
XL    40
L     50
XC    90
C     100
CD    400
D     500
CM    900
M     1000
Numbers are strings of these symbols in descending order. 
In some cases, subtractive notation is used to avoid 
repeated characters. The rules are as follows:
1.) I placed before V or X is one less, 
    so 4 = IV (one less than 5), and 9 is IX (one less than 10)
2.) X placed before L or C indicates ten less, 
    so 40 is XL (10 less than 50) and 90 is XC (10 less than 100).
3.) C placed before D or M indicates 100 less, 
    so 400 is CD (100 less than 500), and 900 is CM (100 less than 1000). """
