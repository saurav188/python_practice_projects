def longestSubsequence(nums):
    calculated={'[]':0}
    def helper(nums):
        if len(nums)==1:
            return 1
        if calculated.get(str(nums)) is not None:
            return calculated[str(nums)]
        current_longest=1
        for j in range(1,len(nums)):
            if nums[j]<nums[0]:
                continue

            if calculated.get(str(nums[j:])) is not None:
                if nums[j]>nums[0]:
                    temp=1+calculated.get(str(nums[j:]))
                else:
                    temp=calculated.get(str(nums[j:]))
            elif nums[j]>nums[0]:
                temp=1+helper(nums[j:])
            else:
                temp=helper(nums[j:])

            if temp>current_longest:
                current_longest=temp
                
        calculated[str(nums)]=current_longest
        return current_longest
    return helper(nums)
print(longestSubsequence([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
#6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
