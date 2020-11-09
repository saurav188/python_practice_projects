class Solution:
    def reverse(self,str,i,j):
        temp=''
        for k in range(j,i-1,-1):
            temp+=str[k]
        return temp

    def reverseWords(self, str):
        start=0
        str+=' '
        for k in range(len(str)):
            if k<len(str) and str[k]==' ':
                str=str[:start]+self.reverse(str,start,k-1)+str[k:]
                start=k+1
        return str
print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah