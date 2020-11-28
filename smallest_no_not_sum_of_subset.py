#Numbers 1 to 6 can all be summed by a subset of the list of numbers, 
#but 7 cannot.

def get_subset_sums(nums):
    subsets=[[]]
    def helper(subsets,nums,i):
        if i>=len(nums):
            return subsets
        temp=[each for each in subsets]
        for j in range(len(temp)):
            temp[j]=temp[j]+[nums[i-1]]
        return helper(subsets+temp,nums,i+1)
    subsets=helper(subsets,nums,1)
    for i in range(len(subsets)):
        temp=0
        for each in subsets[i]:
            temp+=each
        subsets[i]=temp
    return subsets
def findSmallest(nums):
    subset_sums=get_subset_sums(nums)
    for num in range(nums[-1]):
        if num in subset_sums:
            continue
        return num 
    return None

print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7