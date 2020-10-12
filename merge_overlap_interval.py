def merge(intervals):
    for k in range(1,len(intervals)):
        for i in range(len(intervals)-k):
            if intervals[i][0]>intervals[i+1][0]:
                intervals[i],intervals[i+1]=intervals[i+1],intervals[i]
    temp=[item for item in intervals]
    for j in range(len(intervals)-1):
        if intervals[j][1]>intervals[j+1][1]:
            temp.pop(j+1)
    return temp

print(merge([(20, 25), (5, 8), (4, 10),(1, 3)]))
# [(1, 3), (4, 10), (20, 25)]