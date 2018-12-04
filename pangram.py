import string


# long winded way
def ispangram(str1):
    alphabet = list(string.ascii_lowercase)
    matched = []
    # add letters if they match the alphabet
    for letter in str1:
        if letter in alphabet:
            matched.append(letter)
    
    # remove dups
    unique_list = list(dict.fromkeys(matched))
    # sort alphabetically
    sorted_list = sorted(unique_list, key=str.lower)
    # compare to alphabet
    return sorted_list == alphabet

# with "set"

def ispangram_set(str1):
    alphab = set(string.ascii_lowercase)
    phrase = set(str1.lower())

    return alphab <= phrase

print(ispangram('The quick brown fox jumps over the lazy dog'))
print(ispangram_set('The quick brown fox jumps over the lazy dog'))
