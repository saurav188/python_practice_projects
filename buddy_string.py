class Solution:
    def buddyStrings(self, A, B):
        if len(A)!=len(B):
            return False
        countA={}
        countB={}
        difference=0
        for i in range(len(A)):
            letter1= A[i]
            letter2= B[i]
            if letter1!=letter2:
                difference+=1

            if letter1 in countA.keys():
                countA[letter1]+=1
            else:
                countA[letter1]=1

            if letter2 in countB.keys():
                countB[letter2]+=1
            else:
                countB[letter2]=1

        if difference!=2:
            return False

        for key in countA:
            if key not in countB.keys():
                return False
            if countA[key]!=countB[key]:
                return False

        return True        

print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False