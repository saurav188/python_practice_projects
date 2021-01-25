def rotate_list(nums, k):
    for i in range(k):
        nums=[nums[-1]]+nums[:-1]
    return nums

a = [1, 2, 3, 4, 5]
a=rotate_list(a, 3)
print(a)
# [3, 4, 5, 1, 2]