def getProductOf3(arr):
    return arr[0]*arr[1]*arr[2]
def maximum_product_of_three(lst):
    items=[lst[0],lst[1],lst[2]]
    for j in range(3,len(lst)):
        lst_item=lst[j]
        for i in range(len(items)):
            temp=[item for item in items]
            temp[i]=lst_item
            if getProductOf3(temp)>getProductOf3(items):
                if lst_item not in items:
                    items[i]=lst_item
    return getProductOf3(items)

print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
