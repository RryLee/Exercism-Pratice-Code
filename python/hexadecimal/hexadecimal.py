HEXADECIMAL = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15,
}

def hexa(number):
    if any(s.lower() not in HEXADECIMAL.keys() for s in number):
        raise ValueError

    result = 0
    number = number[::-1]
    for i in range(len(number)):
        print result
        result += HEXADECIMAL[number[i].lower()] * (16 ** i)
    return result

print hexa('19ACE')
