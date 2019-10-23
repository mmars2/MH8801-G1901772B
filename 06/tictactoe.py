def TicTacDraw(board):
    inputs = {0:' O ',1:' X ',2:'   '}
    my = 0
    for y in board:
        str = ''
        for x in y:
            str = str + inputs[x] + '|'
        result = str[:-1]
        print(result)
        my = my + 1
        if my != len(board):
            print("-"*(len(board)*4-1))