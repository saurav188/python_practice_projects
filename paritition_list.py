#Given a list of numbers and an integer k, 
#partition/sort the list such that the all 
#numbers less than k occur before k, 
#and all numbers greater than k occur after the number k.

def partition_list(nums, k):
    less_nums=[]
    greater_nums=[]
    for num in nums:
        if num>=k:
            greater_nums.append(num)
        else:
            less_nums.append(num)
    return less_nums+greater_nums

print(partition_list([1,4,3,2,5,2], 3))