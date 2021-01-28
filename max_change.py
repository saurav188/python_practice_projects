#Given a 2d n x m matrix where each cell 
#has a certain amount of change on the floor, 
#your goal is to start from the top left corner 
#mat[0][0] and end in the bottom right corner 
#mat[n - 1][m - 1] with the most amount of change. 
#You can only move either left or down.

def max_change(mat):
    def helper(mat,row_no,col_no):
        no_of_rows=len(mat)
        no_of_cols=len(mat[0])
        last_row=row_no==no_of_rows-1
        last_col=col_no==no_of_cols-1
        if last_row and last_col:
            return mat[row_no][col_no]
        elif last_col:
            return mat[row_no][col_no]+helper(mat,row_no+1,col_no)
        elif last_row:
            return mat[row_no][col_no]+helper(mat,row_no,col_no+1)
        return mat[row_no][col_no]+max(helper(mat,row_no,col_no+1),helper(mat,row_no+1,col_no))
    return helper(mat,0,0)

mat = [
    [0, 3, 0, 2],
    [1, 2, 3, 3],
    [6, 0, 3, 2]
]

print(max_change(mat))
# 13