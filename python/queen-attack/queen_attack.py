def board(w, b):
    if w == b:
        raise ValueError
    if any(x > 7 or x < 0 for x in [w[0], w[1], b[0], b[1]]):
        raise ValueError
    board = [
        '________',
        '________',
        '________',
        '________',
        '________',
        '________',
        '________',
        '________'
    ]
    board[w[0]] = board[w[0]][:w[1]] + 'W' + board[w[0]][w[1] + 1:]
    board[b[0]] = board[b[0]][:b[1]] + 'B' + board[b[0]][b[1] + 1:]

    return board

def can_attack(w, b):
    def can_attack():
        if w[0] == b[0] or b[1] == w[1]:
            return True
        if abs(w[0] - b[0]) == abs(w[1] - b[1]):
            return True
        if abs(w[0] - b[1]) == abs(w[1] - b[0]):
            return True
        return False

    if w == b:
        raise ValueError
    if any(x > 7 or x < 0 for x in [w[0], w[1], b[0], b[1]]):
        raise ValueError
    return can_attack()
