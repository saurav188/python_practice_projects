#tasks = [1, 1, 2, 1]
#cooldown = 2
#output: 7 (order is 1 _ _ 1 2 _ 1)

def findTime(arr, cooldown):
    each_task_cooldown={}
    order=[]
    current_task=[]
    for i in range(len(arr)):
        if arr[i] in current_task:
            order+=['_']*each_task_cooldown[arr[i]]
            order.append(arr[i])
            for key in each_task_cooldown:
                if key!=arr[i]:
                    each_task_cooldown[key]-=(1+each_task_cooldown[arr[i]])
            each_task_cooldown[arr[i]]=2
        else:
            order.append(arr[i])
            current_task.append(arr[i])
            each_task_cooldown[arr[i]]=2
            for key in each_task_cooldown:
                if key!=arr[i]:
                    each_task_cooldown[key]-=1
    return len(order)

print(findTime([1, 1, 2,3, 1,3,1], 2))
# 10