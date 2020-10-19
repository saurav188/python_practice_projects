def first_missing_positive(nums):
    sorted_nums=sorted(nums)
    num=sorted_nums[0]
    while num<=0:
        sorted_nums.pop(0)
        num=sorted_nums[0]

    for i in range(1,sorted_nums[-1]+1):
        if i!=sorted_nums[i-1]:
            return i
            
    return sorted_nums[-1]+1       

print(first_missing_positive([3, 4, -1, 1]))
# 2
