import re

VALIDCHARS = ['+', '-', '*', '|', ' ']

def board(matrix):
    def getCount(i, j):
        count = 0
        if matrix[i][j - 1] == '*':
            count += 1
        if matrix[i][j + 1] == '*':
            count += 1
        if matrix[i - 1][j] == '*':
            count += 1
        if matrix[i + 1][j] == '*':
            count += 1
        if matrix[i + 1][j + 1] == '*':
            count += 1
        if matrix[i + 1][j - 1] == '*':
            count += 1
        if matrix[i - 1][j - 1] == '*':
            count += 1
        if matrix[i - 1][j + 1] == '*':
            count += 1
        return str(count)

    lines = len(matrix)
    columns = len(matrix[0])

    # check matrix valid.
    # 1. no invalid char
    # 2. all columns length same.
    # 3. border
    BORDER_REGEX = '\+\-+\+'
    if re.match(BORDER_REGEX, matrix[0]) == None or re.match(BORDER_REGEX, matrix[lines - 1]) == None:
        raise ValueError("Some Error")

    if any(matrix[i][0] != '|' or matrix[i][columns - 1] != '|' for i in range(1, lines - 1)):
        raise ValueError("Some Error")

    if any(s not in VALIDCHARS for row in matrix for s in row):
        raise ValueError("Some Error")

    if any(len(row) != columns for row in matrix):
        raise ValueError("Some Error")


    for i in range(1, lines - 1):
        for j in range(1, columns - 1):
            if matrix[i][j] != '*' and getCount(i, j) != '0':
                matrix[i] = list(matrix[i])
                matrix[i][j] = getCount(i, j)
                matrix[i] = ''.join(matrix[i])

    return matrix
