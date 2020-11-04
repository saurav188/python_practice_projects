class Solution(object):
    def threeSum(self, nums):
        result=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                for k in range(j+1,len(nums)):
                    if i==j or j==k or i==k:
                        continue
                    if nums[i]+nums[j]+nums[k]==0:
                        result.append([nums[i],nums[j],nums[k]])
        return result
# Test Program
nums = [1, -2, 1, 0, 5]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]