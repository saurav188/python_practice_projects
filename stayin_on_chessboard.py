def is_knight_on_board(x, y, k, cache={}):
    knight_moves=[
        [1,2]  , [2,1]  ,
        [1,-2] , [2,-1] ,
        [-1,-2], [-2,-1], 
        [-2,1] , [-1,2]
    ]
    def helper(x,y,k,in_board,tot_moves):
        if k==0:
            return [in_board,tot_moves]
        response=[in_board,tot_moves]
        for moves in knight_moves:
            is_inside_board=(0<=x+moves[0] and x+moves[0]<7 and 0<=y+moves[1] and y+moves[1]<7)
            if is_inside_board:
                response=helper(x+moves[0],y+moves[1],k-1,response[0]+1,response[1]+1)
            else:
                response[1]+=1
        return response
    response=helper(x,y,k,0,0)
    print(response)
    return response[0]/response[1]

print(is_knight_on_board(0, 0, 2))
# 0.25
# _ _ _ _ _ _ _ _
#|_|_|_|_|_|_|_|_|
#|_|_|_|_|_|_|_|_|
#|_|_|_|_|_|_|_|_|
#|*|_|*|_|_|_|_|_|
#|_|*|_|*|_|_|_|_|
#|*|*|_|_|*|_|_|_|
#|_|_|*|*|_|_|_|_|
#|_|_|*|_|*|_|_|_|
#knight moves with x+-2 y+-1 or y+-2 x+-1 or 