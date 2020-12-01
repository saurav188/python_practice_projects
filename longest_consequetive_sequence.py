def longest_consecutive(nums):
    nums.sort()
    longest_length=0
    temp=1
    for i in range(1,len(nums)):
        if nums[i]-nums[i-1]==1:
            temp+=1
            if temp>longest_length:
                longest_length=temp
        else:
            temp=1
    return longest_length

print(longest_consecutive([100, 4, 200, 1, 3, 2]))
# 4
#[1,2,3,4]