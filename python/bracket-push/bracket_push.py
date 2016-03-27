import re

p = re.compile(u'(\[\]|\{\}|\(\))')

def check_brackets(something):
    if something == '':
        return True

    while p.search(something):
        i = 0
        for m in p.finditer(something):
            something = something[0:m.start() - i] + something[(m.start() + 2 - i):]
            i += 2

    return something == ''

check_brackets("{[]([()])}")
