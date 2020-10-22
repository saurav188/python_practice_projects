def isPalindrome(array):
    i=0
    j=len(array)-1
    while j>i:
        if array[i]!=array[j]:
            return False
        i+=1
        j-=1
    return True
def makePalindrome(array):
    i=0
    j=len(array)-1
    counter=0
    while not isPalindrome(array):
        if array[i]==array[j]:
            i+=1
            j-=1
        else:
            array[i]=array[i]+array[i+1]
            array.pop(i+1)
            counter+=1
            j-=1
    return counter
print(makePalindrome([3 ,2 ,3 ,3 ,5]))