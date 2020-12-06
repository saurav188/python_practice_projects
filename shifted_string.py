def is_shifted(a, b):
    if len(a)!=len(b):
        return False
    pointer1=0
    pointer2=0
    while a[pointer1]!=b[pointer2]:
        pointer2+=1
    for i in range(len(a)):
        if a[pointer1]!=b[pointer2]:
            return False
        pointer1+=1
        pointer2+=1
        if pointer1==len(a):
            pointer1=0
        if pointer2==len(a):
            pointer2=0
    return True
  
print(is_shifted('abcde', 'cdeab'))
# True
#Eg. A = abcde, B = cdeab should return true because 
# A can be shifted 3 times to the right to get B.
#  A = abc and B= acb should return false.