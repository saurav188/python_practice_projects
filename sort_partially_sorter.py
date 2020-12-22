from heapq import heappop, heappush, heapify

def sort_partially_sorted(nums, k):
    length=len(nums)
    heap=nums[:k+1]
    heapify(heap)                    #log(k)
    i=0
    for j in range(k+1,length):
        nums[i]=heappop(heap)
        heappush(heap,nums[j])       #log(k)
        i+=1
    while len(heap)>0:
        nums[i]=heappop(heap)
        i+=1
    return nums
print(sort_partially_sorted([3, 2, 6, 5, 4], 2))
# [2, 3, 4, 5, 6]