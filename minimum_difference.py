#minimum difference between the max and 
#..min item in the array of given length

def minimum_difference(array,k):
    array.sort()
    pointer1=0
    pointer2=len(array)-1
    while pointer2-pointer1>=k:
        temp=array[pointer2]-array[pointer1]
        if (array[pointer2]-array[pointer1+1])>(array[pointer2-1]-array[pointer1]):
            pointer2-=1
        else:
            pointer1+=1
    return array[pointer2]-array[pointer1]

print(minimum_difference([7 ,3 ,2 ,4 ,9 ,12 ,56],3))