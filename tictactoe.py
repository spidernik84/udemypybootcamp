

tabledict = { '1': '1', '2': '2', '3': '3',
              '4': '4', '5': '5', '6': '6',
              '7': '7', '8': '8', '9': '9' }

global winner
winner = False

current_player = 1


def print_board():
    print('{} | {} | {}'.format(tabledict['1'],tabledict['2'],tabledict['3']))
    print('---------')
    print('{} | {} | {}'.format(tabledict['4'],tabledict['5'],tabledict['6']))
    print('---------')
    print('{} | {} | {}'.format(tabledict['7'],tabledict['8'],tabledict['9']))


def checkmatch():
    if tabledict['1'] == tabledict['2'] == tabledict['3']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['1'] == tabledict['5'] == tabledict['9']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['1'] == tabledict['4'] == tabledict['7']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['3'] == tabledict['5'] == tabledict['7']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['2'] == tabledict['5'] == tabledict['8']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['4'] == tabledict['5'] == tabledict['6']:
        # global winner 
        print('you win!')
        winner = True
    elif tabledict['7'] == tabledict['8'] == tabledict['9']:
        # global winner 
        print('you win!')
        winner = True



while True:
    print_board()
    input_numb = input('Ready player {}? Please enter your number: '.format(current_player))

    if current_player == 1:
        player_mark = 'x'
    else:
        player_mark = 'o'

    tabledict[input_numb] = player_mark

    print(tabledict)

    checkmatch()
    print(winner)

    if winner:
        break
    
    current_player = current_player % 2 + 1


print('Congratulations Player {}, you won!'.format(player_mark))


# def print_board(cella1):
#     line = '{} | {} | {}'
#     divider = '----------'
#     print(cella1)
    # print(line.format(cella1, cella2, cella3))
    # print(divider)
    # print(line.format(b1,b2,b3))
    # print(divider)
    # print(line.format(c1,c2,c3))

