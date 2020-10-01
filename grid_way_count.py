#You 2 integers n and m representing an n by m grid, 
#determine the number of ways you can get from the 
#top-left to the bottom-right of the matrix y going 
#only right or down.

def helper(m,n,x,y):
    if x==m or y==n:
        return 0
    if x==m-1 and y==n-1:
        return 1
    return helper(m,n,x+1,y)+helper(m,n,x,y+1)

def num_ways(m, n):
    return helper(m,n,0,0)

print(num_ways(3, 3))
# 2


#                    (0,0)
#               /              \
#           (1,0)             (0,1)
#          /     \          /       \
#        (2,0)   (1,1)   (1,1)        (0,2)
# recurr until both x and y coordinates are less than m and n
# if (x,y) is (m-1,n-1) return +1 else +0  
