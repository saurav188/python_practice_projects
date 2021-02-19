def missing_ranges(nums, low, high):
    result=[]
    num1=1
    num2=1
    for num in nums:
        if num>num1:
            num2+=1
            while num2<num:
                num2+=1
            result.append((num1+1,num2-1))
            num1=num2
    return result

  
print(missing_ranges([1, 3, 5, 10], 1, 10))
# [(2, 2), (4, 4), (6, 9)]