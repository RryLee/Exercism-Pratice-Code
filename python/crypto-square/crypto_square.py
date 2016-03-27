from math import sqrt

def encode(code):
    code = filter(lambda x: x.isalnum(), code).lower()
    length = len(code)
    if length == 0:
        return ''

    i = int(sqrt(length))
    if length % i == 0:
        limit = i
    else:
        limit = i + 1

    secret = ''
    maxtrix = [code[i:i + limit] for i in range(0, length, limit)]

    for i in range(limit):
        row = ''
        for s in maxtrix:
            try:
                row += s[i]
            except IndexError:
                pass
        secret += row + ' '
    return secret.rstrip()
