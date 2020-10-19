#You are given a hash table where the key is a course code, 
#and the value is a list of all the course codes that are 
#prerequisites for the key. Return a valid ordering in which 
#we can complete the courses. If no such ordering exists, return NULL.

def courses_to_take(courses):
    def helper(courses,key,result,visited):
        visited[key]=True
        for course in courses[key]:
            if visited[course]==False:
                helper(courses,course,result, visited)
        result.append(key)
        
    result=[]
    visited={key:False for key in courses}
    for key in courses:
        if visited[key]==False:
            helper(courses,key,result, visited)
    return result

courses = {
  'CSC300': ['CSC100', 'CSC200'], 
  'CSC200': ['CSC100'], 
  'CSC100': []
}
print(courses_to_take(courses))
# ['CSC100', 'CSC200', 'CSC300']
#using topological sort