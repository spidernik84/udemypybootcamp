'''
Simple TicTacToe implementation
'''

import random

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)

def player_input():
    marker = ''

    while not (marker == 'O' or marker == 'X'):
        marker = input('Please pick X or O: ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


# player_input()

def place_marker(board,marker,position):
    board[position] = marker

# place_marker(test_board,'$',8 )
# display_board(test_board)

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

print(win_check(test_board,'O'))

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def check_available(board,position):
    return board[position] == ' '


def check_board_full(board):
    for cell in len(board):
        if check_available(board,cell):
            return False
        else:
            return True

def player_choice(board):
    position = 0
    while position not in range(1,10) or not check_available(board,position):
        position = int(input('Choose your next position: (1-9) '))
    
    return position

def replay():
    return input("Play again? (y/n): ") == "y".lower()



# -------------------------
#           MAIN
# -------------------------

greeting = 'Welcome to TicTacToe'

while True:
    print(greeting)
    print('-' * len(greeting))

    TheBoard = [' '] * 10

    game_on = True

    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + " plays first. Go!")

    while game_on:
        if turn == "Player 1":
            # Player 1
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,player1_marker,position)

            if win_check(TheBoard,player1_marker):
                display_board(TheBoard)
                print('You won!')
                game_on = False
            else:
                if check_board_full(TheBoard):
                    display_board(TheBoard)
                    print('The game is a draw...')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player 2
            display_board(TheBoard)
            position = player_choice(TheBoard)
            place_marker(TheBoard,player2_marker,position)

            if win_check(TheBoard,player2_marker):
                display_board(TheBoard)
                print('You won!')
                game_on = False
            else:
                if check_board_full(TheBoard):
                    display_board(TheBoard)
                    print('The game is a draw...')
                    break
                else:
                    turn = 'Player 1'
    if not replay():
        break