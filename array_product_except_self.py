def products(nums):
    tot_product=1
    for i in nums:
        tot_product*=i
    temp=[]
    for i in nums:
        temp.append(tot_product/i)
    return temp

print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]