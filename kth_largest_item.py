def merge(arr1,arr2):
    arr1_i=0
    arr2_i=0
    result=[]
    while arr1_i<len(arr1) and arr2_i<len(arr2):
        if arr1[arr1_i]<arr2[arr2_i]:
            result.append(arr1[arr1_i])
            arr1_i+=1
        elif arr1[arr1_i]>arr2[arr2_i]:
            result.append(arr2[arr2_i])
            arr2_i+=1
        else:
            result.append(arr1[arr1_i])
            arr1_i+=1
            result.append(arr2[arr2_i])
            arr2_i+=1
    while arr1_i<len(arr1):
        result.append(arr1[arr1_i])
        arr1_i+=1
    while arr2_i<len(arr2):
        result.append(arr2[arr2_i])
        arr2_i+=1
    return result

def mergeSort(array):
    if len(array)==1:return array
    mid_index=len(array)//2
    return merge(mergeSort(array[:mid_index]),mergeSort(array[mid_index:]))

def findKthLargest(nums, k):
    sorted_nums=mergeSort(nums)
    print(sorted_nums)
    return sorted_nums[len(sorted_nums)-k]

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5

#sort it and find the kth last largest item O(nlogn)