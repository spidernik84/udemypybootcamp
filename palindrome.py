
# The stupid/Nicola way:
def palindrome(word):
    word_no_spaces = []
    # skip spaces
    for letter in word:
        if letter != ' ':
            word_no_spaces.append(letter)

    firsth  = word_no_spaces[:int(len(word_no_spaces)/2)]

    # check for even words
    if len(word_no_spaces) % 2 == 0:
        secondh =  word_no_spaces[int(len(word_no_spaces)/2):]
    else:
        # skip mid letter and compare rest
        secondh =  word_no_spaces[int((len(word_no_spaces)/2)+1):]
    # check first half against reverse second half
    if firsth == secondh[::-1]:
        print('true')
    else:
        print('false')


# the pythonic, right way:
def palindrome_light(word):
    return word == word[::-1]

palindrome('helleha')
palindrome_light('helleha')