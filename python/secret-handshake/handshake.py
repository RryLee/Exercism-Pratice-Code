MAXLIMIT = 31
MINLIMIT = 1

def handshake(number):
    def is_binary(n):
        return all(i.isdigit() and 0 <= int(i) <= 1 for i in str(n))

    if is_binary(number):
        if int(str(number), 2) > MAXLIMIT or int(str(number), 2) < MINLIMIT:
            return []
        number = str(number)[::-1]
    else:
        number = int(number)
        if number > MAXLIMIT or number < MINLIMIT:
            return []
        number = str(bin(number))[2::][::-1]

    result = list()
    i = 0
    while i < len(number):
        if number[i] == '1':
            if i == 0:
                result.append('wink')
            elif i == 1:
                result.append('double blink')
            elif i == 2:
                result.append('close your eyes')
            elif i == 3:
                result.append('jump')
            elif i == 4:
                result.reverse()
        i += 1

    return result

WORDS = [
    'wink',
    'double blink',
    'close your eyes',
    'jump'
]

NOTORDERED = 0
SMALLTOBIG = 1
BIGTOSMALL = 2

def check_order(secret):
    ordered = SMALLTOBIG
    if len(secret) != 1:
        ordered = SMALLTOBIG if WORDS.index(secret[1]) - WORDS.index(secret[0]) > 0 else BIGTOSMALL

        if ordered == SMALLTOBIG:
            for i in range(1, len(secret) - 1):
                if WORDS.index(secret[i]) > WORDS.index(secret[i + 1]):
                    ordered = NOTORDERED
                    break
        else:
            for i in range(1, len(secret) - 1):
                if WORDS.index(secret[i]) < WORDS.index(secret[i + 1]):
                    ordered = NOTORDERED
                    break
    return ordered

def format(number):
    while number[0] == '0':
        number = number[1::]
    return number

def code(secret):
    if any(some not in WORDS for some in secret):
        return '0'

    number = ''
    ordered = check_order(secret)
    if ordered == 0:
        raise Exception
    elif ordered == 1:
        for some in WORDS:
            try:
                pos = secret.index(some)
                number = '1' + number
            except Exception as e:
                number = '0' + number
    else:
        for some in WORDS:
            try:
                pos = secret.index(some)
                number = '1' + number
            except Exception as e:
                number = '0' + number
        number = '1' + number

    return format(number)

# print code(['close your eyes', 'jump'])
