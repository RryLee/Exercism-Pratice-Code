NTHDIGIT = [
    'first',
    'second',
    'third',
    'fourth',
    'fifth',
    'sixth',
    'seventh',
    'eighth',
    'ninth',
    'tenth',
    'eleventh',
    'twelfth'
]

STUFFS = [
    'a Partridge',
    'two Turtle Doves',
    'three French Hens',
    'four Calling Birds',
    'five Gold Rings',
    'six Geese-a-Laying',
    'seven Swans-a-Swimming',
    'eight Maids-a-Milking',
    'nine Ladies Dancing',
    'ten Lords-a-Leaping',
    'eleven Pipers Piping',
    'twelve Drummers Drumming'
]

def getstuffs(n):
    stuffs = STUFFS[0]
    if n != 0:
        stuffs = ', and ' + stuffs
        stuffs = ', '.join(STUFFS[1:1+n][::-1]) + stuffs

    return stuffs

def sing():
    return verses(1, 12)

def verse(n):
    return "On the %s day of Christmas my true love gave to me, %s in a Pear Tree.\n" % (NTHDIGIT[n - 1], getstuffs(n - 1))

def verses(n, m):
    lyrics = ''
    while n <= m:
        lyrics += verse(n) + '\n'
        n += 1
    return lyrics
