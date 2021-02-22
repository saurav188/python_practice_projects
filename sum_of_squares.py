import math

def square_sum(n):
    def helper(n,visited):
        print(visited)
        if math.sqrt(n)%1==0:
            visited[n]=1
            return 1
        i=1
        temp=float('inf')
        while i**2<n:
            temp2=helper(n-(i**2),visited)
            visited[n-(i**2)]=temp2
            temp=min(temp,temp2)
            i+=1
        return temp+1
    visited={}
    return helper(n,visited)
print(square_sum(13))
# Min sum is 3**2 + 2**2
# 2