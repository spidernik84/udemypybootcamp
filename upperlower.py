def up_low(s):
    counter = {'lowers': 0, 'uppers': 0}
    # blacklist = ['!', '?', '.', ',', ':', ';', ' ']
    for letter in s:
        if letter.isupper():
            counter['uppers'] += 1
        elif letter.islower():
            counter['lowers'] += 1
        else:
            pass
    print("Uppercase: {} / Lowercase: {}".format(counter['uppers'], counter['lowers']))


s = 'hello Mr. Rogers, how are you this Tuesday? Are you ok?'


up_low(s)