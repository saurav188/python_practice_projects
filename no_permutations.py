def fact(num):
    temp=1
    for i in range(1,num+1):
        temp*=i
    return temp
def permute(nums):
    indexes=[i for i in range(len(nums))]
    result=[]
    for each in range(fact(len(indexes))):
        temp=[]
        for index in indexes:
            temp.append(nums[index])
        result.append(temp)
        x=0
        for i in range(len(indexes)-1,-1,-1):
            if indexes[i]>indexes[i-1]:
                x=i-1
                break
        y=x+1
        for j in range(x+2,len(indexes)):
            if indexes[j]>indexes[x]:
                y=j
        indexes[x],indexes[y]=indexes[y],indexes[x]
        indexes=indexes[:x+1]+indexes[x+1:][::-1]
    return result
print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]