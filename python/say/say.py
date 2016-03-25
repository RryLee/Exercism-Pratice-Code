digits = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    0: 'zero'
}

teens = {
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
}

tens = {
    2: 'twenty',
    3: 'thirty',
    4: 'forty',
    5: 'fifty',
    6: 'sixty',
    7: 'seventy',
    8: 'eighty',
    9: 'ninety',
}

def say_teens(num):
    norm = num % 1e2
    if norm < 10:
        return digits[norm % 10]
    elif norm in range(10, 19):
        return teens[norm]

    single_digit = digits[norm % 10]

    return tens[int(norm / 10)] + ('-' + str(single_digit) if single_digit != 'zero' else '')

def say_hundreds(num):
    norm = num % 1000
    if norm < 1e2:
        return say_teens(num)

    curr_l = digits[norm/100] + ' hundred'
    next_l = say_teens(norm)

    return curr_l if next_l == 'zero' else curr_l + ' and ' + next_l


def say_thousands(num):
    norm = num % 1000000
    if norm < 1e3:
        return say_hundreds(num)

    curr_l = say_hundreds(norm / 1000) + ' thousand'
    next_l = say_hundreds(norm)

    return curr_l if next_l == 'zero' else curr_l + ' ' + next_l

def say_millions(num):
    norm = num % 1000000000
    if norm < 1e6:
        return say_thousands(num)

    curr_l = say_hundreds(int(norm / 1e6)) + ' million'
    next_l = say_thousands(norm)

    if (norm % 1e5) < 1e3 and next_l != 'zero':
        curr_l += ' and ' + next_l
    elif next_l != 'zero':
        curr_l += ' ' + next_l

    return curr_l

def say_billions(num):
    norm = num % 1e12
    if norm < 1e9:
        return say_millions(num)
    curr_l = say_thousands(norm / 1e9) + ' billion'
    next_l = say_millions(norm)

    return curr_l if next_l == 'zero' else curr_l + ' ' + next_l

def say(num):
    if 0 > num or num >= 1e12:
        raise AttributeError

    return say_billions(num)
