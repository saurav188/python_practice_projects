#return min no of rooms required for the lectures
def quicksort(tuples):
    for i in range(len(tuples)):
        for j in range(1,len(tuples)):
            if tuples[j-1][0]>tuples[j][0]:
                tuples[j-1],tuples[j]=tuples[j],tuples[j-1]
    return tuples

def no_rooms(lectures):
    #sort the lectures
    lectures=quicksort(lectures)
    no_of_rooms=0
    visited=[False for i in range(len(lectures))]
    for i in range(len(lectures)):
        if visited[i]:
            continue
        visited[i]=True
        no_of_rooms+=1
        temp=lectures[i][1]
        for j in range(i+1,len(lectures)):
            lecture_overlaps=temp>lectures[j][0]
            if not lecture_overlaps:
                visited[j]=True
                temp=lectures[j][1]
    return no_of_rooms

print(no_rooms([(30, 75), (0, 50), (60, 150)]))
#[(30, 75), (0, 50), (60, 150)] should return 2.