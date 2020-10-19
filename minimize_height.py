def minimize_height(array,k):
    min_height=min(array)
    resulted_array=[]
    for each in array:
        if each-k<=min_height:
            resulted_array.append(each+k)
        else:
            resulted_array.append(each-k)
    return max(resulted_array)-min(resulted_array)

print(minimize_height([1, 5, 8, 10],2))