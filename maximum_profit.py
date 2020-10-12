def buy_and_sell(arr):
    min=0
    for i in range(1,len(arr)):
        if arr[min]>arr[i]:
            min=i
    max=min
    for j in range(min+1,len(arr)):
        if arr[max]<arr[j]:
            max=j
    return arr[max]-arr[min]
    
print(buy_and_sell([9, 11, 8, 5, 7, 10]))
# 5