import math

def running_median(stream):
    result=[]
    for i in range(1,len(stream)+1):
        array=stream[0:i]
        array.sort()#O(nlogn)
        length=len(array)
        is_even=length%2==0
        if is_even:
            mid_index=math.floor(length/2)
            median=(array[mid_index-1]+array[mid_index])/2
        else:
            mid_index=math.floor(length/2)+1
            median=array[mid_index-1]
        result.append(median)
    print(result)
running_median([2, 1, 4, 7, 2, 0, 5])
# 2 1.5 2 3.0 2 2.0 2