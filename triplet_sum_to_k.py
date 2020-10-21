def triplet_sum(array,k):
    array.sort()
    length=len(array)
    for i in range(length):
        pointer1=i+1
        pointer2=length-1
        while pointer1<pointer2:
            temp=array[i]+array[pointer1]+array[pointer2]
            if temp==k:
                return (array[i],array[pointer1],array[pointer2])
            elif temp>k:
                pointer2-=1
            elif temp<k:
                pointer1+=1
    return None

print(triplet_sum([1 ,2 ,4 ,3 ,6],10))
