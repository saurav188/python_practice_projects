def calculate_capacity(arr,border1,border2):
    if border2-border1<=1:
        return 0
    max_capa=min(arr[border1],arr[border2])
    capacity=0
    for i in range(border1+1,border2):
        capacity+=(max_capa-arr[i])
    return capacity
def capacity(arr):
    border1=None
    height1=0
    border2=None
    height2=0
    capacity=0
    for i in range(len(arr)):
        if border1==None:
            border1=i
            height1=arr[border1]
        elif border2 is None:
            if arr[i]>height2:
                border2=i
                height2=arr[border2]
        else:
            if arr[i]>=arr[border2]:
                border2=i
            else:
                capacity+=calculate_capacity(arr,border1,border2)
                border1=border2
                height1=arr[border1]
                height2=0
                border2=None
    return capacity

print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
#        X               
#    X███XX█X              
# 0X█XX█XXXXXX                   
# [0,1,0,2,1,0,1,3,2,1,2,1]

#item in array
#border1,2=0,None
#if border2=None => if item>boder1 => border2=item
#else => if item>=border2 => border2=item
#                    else => calculte_capcity between border1 and border2
#                          > and add it to total capacity
#                          > border1=item
#                          > border2=None