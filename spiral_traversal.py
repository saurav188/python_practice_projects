def matrix_spiral_print(M):
    no_of_row=len(M)
    initial_no_of_row=len(M)
    initial_no_of_column=len(M[0])
    no_of_column=len(M[0])
    visited=[[False for i in range(no_of_column)] for j in range(no_of_row)]
    row_no=0
    column_no=0
    next_no=M[row_no][column_no]
    visited[row_no][column_no]=True
    horizontal_direction=1
    vertical_direction=1
    while next_no is not None:
        print(next_no,end=' ')
        if horizontal_direction==1 and vertical_direction==1:
            if column_no+1<no_of_column:
                column_no+=horizontal_direction
            elif row_no+1<no_of_row:
                row_no+=vertical_direction
            else:
                horizontal_direction=-1
                vertical_direction=-1
                column_no+=horizontal_direction
                no_of_column-=1
                no_of_row-=1

        elif horizontal_direction==-1 and vertical_direction==-1:
            if column_no>initial_no_of_column-no_of_column-1:
                column_no+=horizontal_direction
            elif row_no>initial_no_of_row-no_of_row:
                row_no+=vertical_direction
            else:
                horizontal_direction=1
                vertical_direction=1
                column_no+=horizontal_direction
                
        next_no=M[row_no][column_no]
        if visited[row_no][column_no]:
            next_no=None
        else:
            visited[row_no][column_no]=True
        
    return 

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]
print('1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12')
matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12