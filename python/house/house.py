SONG = [
    'that lay in the house that Jack built.',
    'that ate the malt\n',
    'that killed the rat\n',
    'that worried the cat\n',
    'that tossed the dog\n',
    'that milked the cow with the crumpled horn\n',
    'that kissed the maiden all forlorn\n',
    'that married the man all tattered and torn\n',
    'that woke the priest all shaven and shorn\n',
    'that kept the rooster that crowed in the morn\n',
    'that belonged to the farmer sowing his corn\n',
    'This is the horse and the hound and the horn\n'
]

def verse(n):
    lyrics = ''
    if n == 0:
        return 'This is the house that Jack built.'
    if n == 1:
        lyrics += 'This is the malt\n'
    if n == 2:
        lyrics += 'This is the rat\n'
    if n == 3:
        lyrics += 'This is the cat\n'
    if n == 4:
        lyrics += 'This is the dog\n'
    if n == 5:
        lyrics += 'This is the cow with the crumpled horn\n'
    if n == 6:
        lyrics += 'This is the maiden all forlorn\n'
    if n == 7:
        lyrics += 'This is the man all tattered and torn\n'
    if n == 8:
        lyrics += 'This is the priest all shaven and shorn\n'
    if n == 9:
        lyrics += 'This is the rooster that crowed in the morn\n'
    if n == 10:
        lyrics += 'This is the farmer sowing his corn\n'
    if n == 11:
        lyrics += 'This is the horse and the hound and the horn\n'
    temp = ''
    for i in range(n):
        temp = SONG[i] + temp
    return lyrics + temp

def rhyme():
    return '\n\n'.join([verse(i) for i in range(12)])
