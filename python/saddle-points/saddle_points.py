import sys

def saddle_points(inp):
    def column(i):
        return [row[i] for row in inp]

    if len(inp) == 0:
        return set()

    lines = len(inp[0])
    if any(len(row) != lines for row in inp):
        raise ValueError

    points = set()
    i = 0
    for row in inp:
        j = 0
        for num in row:
            if max(row) == num and min(column(j)) == num:
                points.add((i, j))
            j += 1
        i += 1
    return points
