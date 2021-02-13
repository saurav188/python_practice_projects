def rotate(mat):
    no_row=len(mat)
    no_col=len(mat[0])
    result_mat=[[True for i in range(no_row)] for j in range(no_col)]
    for i in range(no_row):
        for j in range(no_col):
            result_mat[j][no_col-1-i]=mat[i][j]
    return result_mat

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Looks like
# 1 2 3
# 4 5 6
# 7 8 9

# Looks like
# 7 4 1
# 8 5 2
# 9 6 3
print(rotate(mat))
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]