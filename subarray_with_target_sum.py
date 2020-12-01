def getsubarray(list):
    def helper(subarray,index):
        if index==len(list):
            return subarray
        temp=[each for each in subarray]
        for i in range(len(subarray)):
            temp[i]=temp[i]+[list[index]]
        subarray+=temp
        return helper(subarray,index+1)
    return helper([[]],0)
def find_continuous_k(list, k):
    subarrays=getsubarray(list)
    i=0
    for subarray in subarrays:
        i+=1
        temp=0
        for each in subarray:
            temp+=each
        if temp==k:
            return subarray
    return None

print(find_continuous_k([1, 3, 2, 5, 7, 2], 14))
# [2, 5, 7]
#O(2**n+1)