import numpy as np


def drawer(board,size=3):
    variables = []
    for line in board:
        for single in line:
            variables.append(single)
    verticals = []
    for x in range(0,len(variables)):
        verticals.append('| %s ' % variables[x])
    last = '|'
    for i in range(0,9,3):
        print(' ---'*size)
        joiner = ''.join(verticals[0+i:3+i])
        print(''.join([joiner,last]))
    print(' ---'*size)


    #second example
    '''print(variables)
    horizontal = ' ---'
    vertical = '|   '
    board = (horizontal * size) + ' ' + '\n' + (vertical * size) + '|'
    sizer_board = ((board + '\n') * size) + horizontal * size
    print(sizer_board)'''

def tic_tac_toe_game():
    win = 0
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    plansza = drawer(matrix)
    while win == 0:
        '''for line in matrix:
            print(line)'''
        print('Player 1: please write 1 in a correct position -- first row, second col ')
        player_1_row = int(input('Input row: '))
        player_1_col = int(input('Input col: '))
        matrix[player_1_row][player_1_col] = 1
        print('Player 2: please write 2 in a correct position -- first row, second col ')
        player_2_row = int(input('Input row: '))
        player_2_col = int(input('Input col: '))
        if [player_1_row, player_1_col] == [player_2_col, player_2_row]:
            print('This position is taken')
            player_2_row = int(input('Input row: '))
            player_2_col = int(input('Input col: '))
        matrix[player_2_row][player_2_col] = 2
        win = check_winner_rows(matrix)
        plansza = drawer(matrix)
    return matrix

def check_winner_rows(matrix):
    win = 0
    print("")
    print("I check who win the game")
    for i in range(3):
        set_rows = set(matrix[i])
        if len(set_rows) == 1 and matrix[0][i] != 0:
            if set_rows == {1}:
                print("Player 1 won the game :)")
                win = 1
            elif set_rows == {2}:
                print("Player 2 won the game :)")
                win = 1

    cols = np.transpose(matrix)
    for i in range(3):
        set_cols = set(cols[i])
        if len(set_cols) == 1 and matrix[0][i] != 0:
            if set_cols == {1}:
                print("Player 1 won the game :)")
                win = 1
            elif set_cols == {2}:
                print("Player 2 won the game :)")
                win = 1
    return win


def run():
    tic_tac_toe_game()


if __name__ == '__main__':
    run()
