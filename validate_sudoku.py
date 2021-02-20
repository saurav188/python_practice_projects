def validate_sudoku(board):
    temp1={
        1:None,2:None,3:None,
        4:None,5:None,6:None,
        7:None,8:None,9:None,
    }
    temp2={
        1:None,2:None,3:None,
        4:None,5:None,6:None,
        7:None,8:None,9:None,
    }
    for index in range(9):
        for i in range(9):
            if board[index][i]==' ' or board[i][index]:
                continue
            #row_check
            if temp1[board[index][i]]==True:
                return False
            else:
                temp1[board[index][i]]=True
            #column_check
            if temp2[board[i][index]]==True:
                return False
            else:
                temp2[board[i][index]]=True
        temp1={
            1:None,2:None,3:None,
            4:None,5:None,6:None,
            7:None,8:None,9:None,
        }
        temp2={
            1:None,2:None,3:None,
            4:None,5:None,6:None,
            7:None,8:None,9:None,
        }
    for i in range(3):
        for j in range(3):
            for k in range(i*3,(i*3)+3):
                for l in range(j*3,(j*3)+3):
                    if board[k][l]==' ':
                        continue
                    if temp1[board[k][l]]==True:
                        return False
                    else:
                        if board[k][l]!=' ':
                            temp1[board[k][l]]=True
            temp1={
                1:None,2:None,3:None,
                4:None,5:None,6:None,
                7:None,8:None,9:None,
            }
    return True
board = [
    [5, ' ', 4, 6, 7, 8, 9, 1, 2],
    [6, ' ', 2, 1, 9, 5, 3, 4, 8],
    [1,   9, 8, 3, 4, 2, 5, 6, 7],
    [8,   5, 9, 7, 6, 1, 4, 2, 3],
    [4,   2, 6, 8, 5, 3, 7, 9, 1],
    [7,   1, 3, 9, 2, 4, 8, 5, 6],
    [9,   6, 1, 5, 3, 7, 2, 8, 4],
    [2,   8, 7, 4, 1, 9, 6, 3, 5],
    [3,   4, 5, 2, 8, 6, 1, 7, 9],
]

print(validate_sudoku(board))