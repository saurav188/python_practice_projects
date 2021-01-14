#Given a nxm matrix, find the number of ways someone can go 
#from the top left corner to the bottom right corner. 
#You can assume the two corners will always be 0.

def paths_through_maze(maze):
    rows=len(maze)
    columns=len(maze[0])
    def helper(maze,x,y):
        is_right_bottom=x==columns-1 and y==rows-1
        if is_right_bottom:
            return 1
        exceeds_the_maze=x>=columns or y>=rows
        if exceeds_the_maze:
            return 0
        hits_the_wall=maze[y][x]==1
        if hits_the_wall:
            return 0
        return helper(maze,x+1,y)+helper(maze,x,y+1)
    return helper(maze,0,0)


print(paths_through_maze([[0, 0, 0],
                          [1, 0, 1],
                          [0, 0, 0]]))
# 2