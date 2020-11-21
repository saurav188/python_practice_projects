def climb_ladder(no_steps,array_of_steps):
    steps=[0 for i in range(no_steps+1)]
    steps[0]=1
    for i in range(1,no_steps+1):
        temp=0
        for j in array_of_steps:
            if i-j>=0:
                temp+=steps[i-j]
        steps[i]=temp
    return steps[no_steps]

steps=3
array_of_steps=[1,2]
print(climb_ladder(steps,array_of_steps))

#return climb
#1+1+2+3+5+8+13