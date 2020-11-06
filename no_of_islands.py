class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def DFS(self,gird,r,c,visited):
        visited[r][c]=True
        row_neighbour   =[-1, 0, 1, 0]
        column_neighbour=[ 0, 1, 0,-1]
        for i in range(4):
            is_inrange=self.inRange(grid,r+row_neighbour[i],c+column_neighbour[i])==True
            if is_inrange:
                is_visited=visited[r+row_neighbour[i]][c+column_neighbour[i]]
                is_island=grid[r+row_neighbour[i]][c+column_neighbour[i]]==1
            else:
                is_visited=True
                is_island=False
            if is_inrange and not is_visited and is_island:
                self.DFS(grid,r+row_neighbour[i],c+column_neighbour[i],visited)

    def numIslands(self, grid):
        visited=[[False for i in range(len(grid[0]))] for  j in range(len(grid))]
        island_count=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if visited[i][j]==True:
                    continue 
                if grid[i][j]==1:
                    self.DFS(grid,i,j,visited) 
                    island_count+=1

        return island_count

grid = [[1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))