def masteryoda(text):
    newtext = text.split(' ')
    newtext.reverse()
    return(' '.join(newtext))


print(masteryoda('I am home today'))