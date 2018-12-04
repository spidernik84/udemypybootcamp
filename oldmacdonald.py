def oldmacdonald(name):
    first_half = str(name[0:3].capitalize())
    second_half = str(name[3:].capitalize())
    return str(first_half + second_half)

print(oldmacdonald('macdonald'))