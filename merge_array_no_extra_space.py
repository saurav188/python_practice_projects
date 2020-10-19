def merge(arr1,arr2):
    arr2_len=len(arr2)
    arr1_i=0
    arr2_i=0
    while arr1_i<len(arr1) and arr2_i<arr2_len:
        if arr1[arr1_i]<arr2[arr2_i]:
            arr1.insert(arr1_i+1,arr2[arr2_i])
        else:
            arr1.insert(arr1_i,arr2[arr2_i])
        arr1_i+=2
        arr2_i+=1
    return arr1

print(merge([10, 12],[5, 18, 20]))