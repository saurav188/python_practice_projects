#Explanation: Sorting the window (2, 4) which is 
#[7, 5, 6] will also means that the whole list is sorted.

def min_window_to_sort(nums):
    pointer1=0
    pointer2=0
    i=1
    while i<len(nums):
        if pointer1==0 and pointer2==0:
            if nums[i]<nums[i-1]:
                pointer1=i-1
                pointer2=i
        else:
            if nums[pointer1]>nums[i]:
                pointer2=i
        i+=1
    i=0
    while i<pointer1:
        if nums[pointer2]<nums[i]:
            pointer1=i
        i+=1 
    i=len(nums)-1
    while i>pointer2:
        if nums[pointer1]>nums[i]:
            pointer2=i 
        i-=1 
    return (pointer1,pointer2)
  
print(min_window_to_sort([2, 4, 7, 5, 6, 3, 9]))
# (2, 4)