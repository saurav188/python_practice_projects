#You are given a hash table where the key is a course code, 
#and the value is a list of all the course codes that are 
#prerequisites for the key. Return a valid ordering in which 
#we can complete the courses. If no such ordering exists, return NULL.

def courses_to_take(course_to_prereqs,key=None):
    if key==None:
        first_key= next(iter(course_to_prereqs))
    else:
        first_key=key
    prerequities=course_to_prereqs[first_key]
    if len(prerequities)==0:return [first_key]
    result=[]
    for prerequiti in prerequities:
        result+= courses_to_take(course_to_prereqs,prerequiti)
    result= result+[first_key]
    for i in range(len(result)-1,0,-1):
        if result[i] in result[:i]:
            result.remove(result[i])
    return result

courses = {
  'CSC400': ['CSC100', 'CSC200', 'CSC300'], 
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']

#check each course'value taking as a key
#if course need no prequisities add it to result array
#else if prequisities required is in result array add it at the end
#else if prequisities requied is not in result array check the prequisitie 
#as the untill the prequisite can be taken

#               CSC300
#         CSC200      CSC100
#      CSC100                []