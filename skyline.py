newword = []
def myfunc(word):
    for pos,letter in enumerate(word):
        if pos % 2 == 0:
            newword.append(letter.lower)
        else:
            newword.append(letter.upper)
    return newword


print(myfunc('lololololol'))