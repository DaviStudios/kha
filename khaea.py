def kha(string):
    words = string.split()
    hashed = ''
    sep = ''

    for word in words:
        wordv = 31
        for letter in word:
            wordv += (wordv * 31 + ord(letter)) % 31
        hashed += str(wordv) + 'SEP'
    if hashed[0] == '0':
        sep = 'a'
    elif hashed[0] == '1':
        sep = 'b'
    elif hashed[0] == '2':
        sep = 'c'
    elif hashed[0] == '3':
        sep = 'd'
    elif hashed[0] == '4':
        sep = 'e'
    elif hashed[0] == '5':
        sep = 'f'
    elif hashed[0] == '6':
        sep = 'p'
    elif hashed[0] == '7':
        sep = 'y'
    elif hashed[0] == '8':
        sep = 'z'
    elif hashed[0] == '9':
        sep = 'x'
    hashed = hashed.replace('SEP', sep)

    while len(hashed) < 65:
        hashed += sep
    while len(hashed) > 64:
        hashed = hashed[:-1]

    return hashed

def keae(string):
    n = ''
    for i in string:
        n +=str(31 * ord(i)) + '-'
    return n

def kead(string):
    n = ''
    for i in string.split('-'):
        if i:
            rp = round(int(i) / 31)
            n += chr(rp)
    return n
