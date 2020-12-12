def max_area(histogram):
    stack=[0]
    index=1
    max_area=histogram[0]
    while index<len(histogram):
        if histogram[stack[-1]]<=histogram[index]:
            stack.append(index)
            index+=1
        else:
            top=stack.pop()
            max_area=max(max_area,(histogram[top]*(index-(stack[-1] if len(stack)>0 else 1)-1)))
    while len(stack)>0:
        top=stack.pop()
        max_area=max(max_area,(histogram[top]*(index-(stack[-1] if len(stack)>0 else -1)-1)))

    return max_area

print(max_area([1,2,3,4,5]))
