import random as rng
import math
def wanderMove(distance, monster, board, overlay, row, col):
    dir = rng.randrange(1,5)
    if dir == 1 and row > distance \
    and board[row-1][col] == 2:
        overlay[row-distance][col] = monster
    elif dir == 2 and col > distance \
    and board[row][col-distance] == 2:
        overlay[row][col-distance] = monster
    elif dir == 3 and row < len(board)-distance \
    and board[row+1][col] == 2:
        overlay[row+distance][col] = monster
    elif dir == 4 and col < len(board[0])-distance \
    and board[row][col+distance] == 2:
        overlay[row][col+distance] = monster
    else:
        overlay[row][col] = monster
def chaseMove(monster,board,overlay,row,col,recents,playerCoords):
    recents.append((row,col))
    recents.pop(0)
    desireable = [0,0,0,0]
    options = [
        (row-1,col),
        (row+1,col),
        (row,col-1),
        (row,col+1)
    ]
    for i in range(len(options)):
        desireable[i] = \
        math.sqrt((abs(options[i][0]-playerCoords[0])+1)**2 + \
        (abs(options[i][1]-playerCoords[1])+1)**2) if \
        board[options[i][0]][options[i][1]] \
        == 2 else 100000
    smallval = 100000
    for i in range(len(desireable)):
        if i == 0 or desireable[i] < smallval:
            if options[i] not in recents:
                small = i
                smallval = desireable[small]
    try:
        overlay[options[small][0]][options[small][1]] = monster
    except UnboundLocalError:
        overlay[row][col] = monster
