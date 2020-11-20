#Given a list of numbers of size n, where n is greater than 3,
#find the maximum and minimum of the list using 
#less than 2 * (n - 1) comparisons.

def find_min_max(nums):
    max=nums[0]
    min=nums[0]
    for i in range(1,len(nums)):
        if nums[i]>max:
            max=nums[i]
        if nums[i]<min:
            min=nums[i]
    return (min,max)
print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)