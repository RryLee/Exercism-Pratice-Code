from collections import OrderedDict

DIGITTOROMAN = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'),
                (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
                (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def numeral(num):
    roman = ''

    for item in DIGITTOROMAN:
        while num >= item[0]:
            roman += item[1]
            num -= item[0]

    return roman
