def square_numbers(nums):
    result=nums
    pointer=len(nums)-1
    while nums[0]<0:
        while abs(nums[0])<nums[pointer]:
            pointer-=1
        temp=abs(result.pop(0))
        result.insert(pointer,temp)
    for i in range(len(result)):
        result[i]=result[i]**2
    return result

print(square_numbers([-5, -3, -1, 0, 1, 4, 5]))
# [0, 1, 1, 9, 16, 25, 25]