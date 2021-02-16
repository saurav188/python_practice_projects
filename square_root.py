#Given a positive integer, find the square 
#root of the integer without using any built 
#in square root or power functions 
#(math.sqrt or the ** operator). 
#Give accuracy up to 3 decimal points.

def sqrt(x):
    a=0
    b=x
    y=(a+b)/2
    while round(a,3)!=round(b,3):
        if y**2>x:
            b=y
        else:
            a=y
        y=(a+b)/2
    return round(y,3)

print(sqrt(6))