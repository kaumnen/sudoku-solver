board = [

    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5],
    [1,0,2,0,3,0,4,0,5]

]

def printing_board(bo):
    for i in range(len(bo)):
        if i == 3 or i == 6:
            print('- - - - - - - - - - -')
        for j in range(len(bo[0])):
            if j == 3 or j == 6:
                print('| ', end = '')
            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end = '')

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # row, col
