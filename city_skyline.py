#Given a list of building in the form of (left, right, height), 
#return what the skyline should look like. 
#The skyline should be in the form of a list of (x-axis, height), 
#where x-axis is the next point where there is a change in height 
#starting from 0, and height is the new height starting from the x-axis.

def generate_skyline(buildings):
    if buildings==[]:
        return None
    building=buildings.pop(0)
    pointer1=building[0]
    pointer2=building[1]
    height=building[2]
    result=[]
    while len(buildings)>0:
        building=buildings.pop(0)
        #height of next bulding is heigher
        if building[2]>height:
            #next building is smaller in length than current one
            if building[0]>pointer1 and building[1]<pointer2:
                result.append((pointer1,height))
                pointer1=building[0]
                result.append((pointer1,building[2]))
                pointer1=building[1]+1
            #next build exeeds the current building
            elif building[0]>pointer1 and building[1]>pointer2:
                result.append((pointer1,height))
                pointer1=building[0]
                height=building[2]
        #height is same
        elif building[2]==height:
            if pointer2<building[1]:
                pointer2=building[1]
        #height is smaller and exceed the length of the current bulding 
        elif building[2]<height and building[1]>pointer2:
            result.append((pointer1,height))
            pointer1=building[0]+1
            pointer2=building[1]
            height=building[2]

    result.append((pointer1,height))
    return result

#            2 2 2
#            2 2 2
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
#        1 1 2 2 2 1 1
# pos: 1 2 3 4 5 6 7 8 9
print(generate_skyline([(2, 8, 3), (4, 6, 5),(8,10,2)]))
# [(2, 3), (4, 5), (7, 3), (9, 0)]
# three variables pointer1(start),pointer2(end),height
#pointer1=x pointer2=y height=h
#let next be (x,y,h)
#if x>pointer1 and y<pointer1::>pointer1=x,