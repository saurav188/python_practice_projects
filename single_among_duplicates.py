class Solution(object):
    def findSingle(self, nums):
        dict={}
        for num in nums:
            if dict.get(num)!=None:
                dict[num]+=1
                continue
            dict[num]=1
        single=None
        for key in dict:
            if dict[key]==1:
                single=key
        
        return single
nums = [1, 1, 3, 4, 4, 5, 6, 5, 6]
print(Solution().findSingle(nums))
# 3