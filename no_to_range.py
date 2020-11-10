def findRanges(nums):
    start=nums[0]
    output=[]
    for i in range(len(nums)):
        if i+1==len(nums):
            output.append(str(nums[start])+'->'+str(nums[i]))
            continue
        if nums[i+1]-nums[i]>1:
            output.append(str(nums[start])+'->'+str(nums[i]))
            start=i+1
    return output

print(findRanges([0, 1, 2, 5, 7, 9, 10, 11, 15]))