def isSorted(array):
    for i in range(len(array)-1):
        if array[i]>array[i+1]:
            return False
    return True
def sort(array):
    for i in range(1,len(array)):
        for j in range(len(array)-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array
def getNext(array):
    if not isSorted(array):
        return sort(array)
    x=0
    for i in range(len(array)-1):
        if array[i]<array[i+1]:
            x=i
    y=x
    for j in range(x,len(array)):
        if array[j]>array[x]:
            y=j
    array[x],array[y]=array[y],array[x]
    reversed_array=[array[k] for k in range(len(array)-1,x,-1)]
    return array[0:x+1]+reversed_array
print(getNext([1,2,3,4,5]))