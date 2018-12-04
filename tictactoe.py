

tabledict = { '1': ' ', '2': ' ', '3': ' ',
              '4': ' ', '5': ' ', '6': ' ',
              '7': ' ', '8': ' ', '9': ' ' }


current_player = 1



while True:
    input_numb = input('Ready player {}? Please enter your number: '.format(current_player))

    if current_player == 1:
        player_mark = 'x'
    else:
        player_mark = 'o'

    tabledict[input_numb] = player_mark

    print(tabledict)

    current_player = current_player % 2 + 1

# def print_board(cella1):
#     line = '{} | {} | {}'
#     divider = '----------'
#     print(cella1)
    # print(line.format(cella1, cella2, cella3))
    # print(divider)
    # print(line.format(b1,b2,b3))
    # print(divider)
    # print(line.format(c1,c2,c3))

