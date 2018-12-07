

tabledict = { '1': '1', '2': '2', '3': '3',
              '4': '4', '5': '5', '6': '6',
              '7': '7', '8': '8', '9': '9' }
winner = False
current_player = 1
turn = 0

def print_board():
    print('{} | {} | {}'.format(tabledict['1'],tabledict['2'],tabledict['3']))
    print('---------')
    print('{} | {} | {}'.format(tabledict['4'],tabledict['5'],tabledict['6']))
    print('---------')
    print('{} | {} | {}'.format(tabledict['7'],tabledict['8'],tabledict['9']))


def checkmatch():
    global winner 
    if tabledict['1'] == tabledict['2'] == tabledict['3']:
        winner = True
    elif tabledict['1'] == tabledict['5'] == tabledict['9']: 
        winner = True
    elif tabledict['1'] == tabledict['4'] == tabledict['7']: 
        winner = True
    elif tabledict['3'] == tabledict['5'] == tabledict['7']: 
        winner = True
    elif tabledict['2'] == tabledict['5'] == tabledict['8']: 
        winner = True
    elif tabledict['4'] == tabledict['5'] == tabledict['6']: 
        winner = True
    elif tabledict['7'] == tabledict['8'] == tabledict['9']: 
        winner = True



while True:
    print_board()
    input_numb = input('Ready player {}? Please enter your number: '.format(current_player))

    if current_player == 1:
        player_mark = 'x'
    else:
        player_mark = 'o'
    if tabledict[input_numb] != ('x' or 'o'):
        tabledict[input_numb] = player_mark
    else:
        print('That spot is taken!')

    checkmatch()
    if winner:
        break
    turn += 1
    if turn == 9:
        break
    current_player = current_player % 2 + 1

if turn == 9:
    print('Draw...')
else:
    print('Congratulations Player {}, you won!'.format(current_player))

