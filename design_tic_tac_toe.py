""" 
Given n = 3, assume that player 1 is "X" and player 2 is "O" 
board = TicTacToe(3);

board.move(0, 0, 1); -> Returns 0 (no one wins)
|X| | |
| | | |    // Player 1 makes a move at (0, 0).
| | | |

board.move(0, 2, 2); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 2 makes a move at (0, 2).
| | | |

board.move(2, 2, 1); -> Returns 0 (no one wins)
|X| |O|
| | | |    // Player 1 makes a move at (2, 2).
| | |X|

board.move(1, 1, 2); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 2 makes a move at (1, 1).
| | |X|

board.move(2, 0, 1); -> Returns 0 (no one wins)
|X| |O|
| |O| |    // Player 1 makes a move at (2, 0).
|X| |X|

board.move(1, 0, 2); -> Returns 0 (no one wins)
|X| |O|
|O|O| |    // Player 2 makes a move at (1, 0).
|X| |X|

board.move(2, 1, 1); -> Returns 1 (player 1 wins)
|X| |O|
|O|O| |    // Player 1 makes a move at (2, 1).
|X|X|X|
 """

import math

class TicTacToe(object):
    def __init__(self, n):
        self.board=[['' for i in range(n)] for j in range(n)]
        self.size=n
        self.center_row=math.floor(n/2)+1
        self.center_column=math.floor(n/2)+1

    def check_for_win(self, row, col, player):
        #checking row wins
        temp=True
        for i in range(self.size-1):
            temp=temp&(self.board[row][i]==self.board[row][i+1])
        if temp==True:
            return player
        #checking column wins
        temp=True
        for i in range(self.size-1):
            temp=temp&(self.board[i][col]==self.board[i+1][col])
        if temp==True:
            return player
        #checking diagonal win 
        if row==col:
            temp=True
            for i in range(self.size-1):
                temp=temp&(self.board[i][i]==self.board[i+1][i+1])
            if temp==True and temp!='':
                return player
        if row==self.size-1-col:
            temp=True
            for i in range(self.size-1,0,-1):
                temp=temp&(self.board[self.size-1-i][i]==self.board[self.size-i][i-1])
            if temp==True and temp!='':
                return player
        return 'continue'

    def move(self, row, col, player):
        player_sign='X' if player==1 else 'O'
        self.board[row][col]=player_sign
        for each in self.board:
            print(each)
        return self.check_for_win(row,col,player)


board = TicTacToe(3)
print(board.move(0, 0, 1))
print(board.move(0, 2, 2))
print(board.move(2, 2, 1))
print(board.move(1, 1, 2))
print(board.move(2, 0, 1))
print(board.move(1, 0, 2))
print(board.move(2, 1, 1))