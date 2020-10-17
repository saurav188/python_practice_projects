def matrix_spiral_print(M):
    def helper(grid,direction):
        if len(grid)==0:
            return
        no_of_rows=len(grid)
        no_of_columns=len(grid[0])
        if direction==1:
            row=0
            colunm=0
            while row<no_of_rows and colunm<no_of_columns:
                print(grid[row][colunm],end=' ')
                if colunm+1<no_of_columns:
                    colunm+=1
                else:
                    row+=1
            helper([[grid[j][i] for i in range(no_of_columns-1)] for j in range(1,no_of_rows)],-direction)
        else:
            row=no_of_rows-1
            column=no_of_columns-1
            while row>=0 and column>=0:
                print(grid[row][column],end=' ')
                if column>0:
                    column-=1
                else:
                    row-=1
            helper([[grid[j][i] for i in range(1,no_of_columns)] for j in range(no_of_rows-1)],-direction)
    
    direction=1
    helper(grid,direction)

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
print('1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12')
matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12