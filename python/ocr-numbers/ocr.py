import string

NUMBERS = [
    ([' _ ', '| |', '|_|', '   ']), # 0
    (['   ', '  |', '  |', '   ']), # 1
    ([' _ ', ' _|', '|_ ', '   ']), # 2
    ([' _ ', ' _|', ' _|', '   ']), # 3
    (['   ', '|_|', '  |', '   ']), # 4
    ([' _ ', '|_ ', ' _|', '   ']), # 5
    ([' _ ', '|_ ', '|_|', '   ']), # 6
    ([' _ ', '  |', '  |', '   ']), # 7
    ([' _ ', '|_|', '|_|', '   ']), # 8
    ([' _ ', '|_|', ' _|', '   ']), # 9
]
UNKNOW = '?'

def number(matrix):
    if len(matrix) != 4:
        raise ValueError

    result = ''
    for i in range(0, len(matrix[0]), 3):
        result += get_number([matrix[0][i:i+3],
                              matrix[1][i:i+3],
                              matrix[2][i:i+3],
                              matrix[3][i:i+3],])

    return result

def get_number(matrix):
    # check the matrix
    if any(len(s) != 3 for s in matrix):
        raise ValueError
    if any(x not in "|_ " for s in matrix for x in s):
        return UNKNOW

    try:
        return str(NUMBERS.index(matrix))
    except Exception as e:
        return UNKNOW

def grid(number):
    if any(x not in map(str, string.digits) for x in number):
        raise ValueError

    diagram = ["", "", "", ""]
    for i in number:
        if i == '0':
            diagram[0] += ' _ '
            diagram[1] += '| |'
            diagram[2] += '|_|'
            diagram[3] += '   '
        elif i == '1':
            diagram[0] += '   '
            diagram[1] += '  |'
            diagram[2] += '  |'
            diagram[3] += '   '
        elif i == '2':
            diagram[0] += ' _ '
            diagram[1] += ' _|'
            diagram[2] += '|_ '
            diagram[3] += '   '
        elif i == '3':
            diagram[0] += ' _ '
            diagram[1] += ' _|'
            diagram[2] += ' _|'
            diagram[3] += '   '
        elif i == '4':
            diagram[0] += '   '
            diagram[1] += '|_|'
            diagram[2] += '  |'
            diagram[3] += '   '
        elif i == '5':
            diagram[0] += ' _ '
            diagram[1] += '|_ '
            diagram[2] += ' _|'
            diagram[3] += '   '
        elif i == '6':
            diagram[0] += ' _ '
            diagram[1] += '|_ '
            diagram[2] += '|_|'
            diagram[3] += '   '
        elif i == '7':
            diagram[0] += ' _ '
            diagram[1] += '  |'
            diagram[2] += '  |'
            diagram[3] += '   '
        elif i == '8':
            diagram[0] += ' _ '
            diagram[1] += '|_|'
            diagram[2] += '|_|'
            diagram[3] += '   '
        elif i == '9':
            diagram[0] += ' _ '
            diagram[1] += '|_|'
            diagram[2] += ' _|'
            diagram[3] += '   '
    return diagram
