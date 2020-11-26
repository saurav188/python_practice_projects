def fact(n):
    temp=1
    for i in range(1,n+1):
        temp*=i
    return temp
def get_num(nums,indexes):
    temp=''
    for index in indexes:
        temp+=str(nums[index])
    return int(temp)

def largestNum(nums):
    largest=0
    indexes=[i for i in range(len(nums))]
    for each in range(fact(len(nums))):
        temp=get_num(nums,indexes)
        if largest<temp:
            largest=temp
        x=0
        for i in range(len(indexes)-1,-1,-1):
            if indexes[i]>indexes[i-1]:
                x=i-1
                break
        y=0
        for i in range(len(indexes)-1,-1,-1):
            if indexes[i]>indexes[x]:
                y=i
                break
        indexes[x],indexes[y]=indexes[y],indexes[x]
        indexes=indexes[:x+1]+indexes[x+1:][::-1]
    return largest
print(largestNum([17, 7, 2, 45, 72]))
# 77245217