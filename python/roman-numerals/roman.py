from collections import OrderedDict

DIGITTOROMAN = OrderedDict()
DIGITTOROMAN[1000] = 'M'
DIGITTOROMAN[900] = 'CM'
DIGITTOROMAN[500] = 'D'
DIGITTOROMAN[400] = 'CD'
DIGITTOROMAN[100] = 'C'
DIGITTOROMAN[90] = 'XC'
DIGITTOROMAN[50] = 'L'
DIGITTOROMAN[40] = 'XL'
DIGITTOROMAN[10] = 'X'
DIGITTOROMAN[9] = 'IX'
DIGITTOROMAN[5] = 'V'
DIGITTOROMAN[4] = 'IV'
DIGITTOROMAN[1] = 'I'

def numeral(num):
    roman = ''

    for key, value in DIGITTOROMAN.items():
        print key, value
        while num >= key:
            roman += value
            num -= key

    return roman
