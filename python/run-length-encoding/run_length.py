import re

def encode(code):
    result = ''
    letters = []
    times = []
    current = code[0:1]
    time = 1
    for s in code[1::]:
        if s == current:
            time += 1
        else:
            letters.append(current)
            times.append(time)

            current = s
            time = 1
            continue
    letters.append(current)
    times.append(time)

    print letters
    print times

    for i in range(len(times)):
        if times[i] == 1:
            result += letters[i]
        else:
            result += str(times[i]) + letters[i]

    return result

def decode(code):
    result = ''
    time = ''

    i = 0
    while i < len(code):
        if code[i].isdigit():
            time += code[i]
        else:
            if time == '':
                time = 1
            result += int(time) * code[i]
            time = ''
        i += 1

    return result
