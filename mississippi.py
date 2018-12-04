def missi(text):
    newword = []
    for l in text:
        newword.append(l*3)
    return ''.join(newword)


print(missi('word'))