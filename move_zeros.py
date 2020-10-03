class Solution:
  def moveZeros(self, nums):
    final_index=len(nums)-1
    while nums[final_index]==0:
        final_index-=1
    i=0
    while i<final_index:
        if nums[i]==0:
            nums[i],nums[final_index]=nums[final_index],nums[i]
            final_index-=1
        i+=1
    return nums

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]