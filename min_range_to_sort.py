def findRange(nums):
    def helper(nums,a,b):
        if a>=b+1:
            return None
        highest=max(nums[a:b+1])
        lowest=min(nums[a:b+1])
        if nums[a]==lowest and nums[b]==highest:
            return helper(nums,a+1,b-1)
        elif nums[a]==lowest:
            return helper(nums,a+1,b)
        elif nums[b]==highest:
            return helper(nums,a,b-1)
        else:
            return [a,b]
    return helper(nums,0,len(nums)-1)
print(findRange([1, 7, 9, 5, 7, 8, 10]))
print(findRange([1, 5, 6, 2, 8, 9, 10]))