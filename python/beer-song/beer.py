def song(n, m = 0):
    lyrics = ''
    while n >= m:
        lyrics += verse(n) + "\n"
        n -= 1
    return lyrics

def verse(n):
    lyrics = ''
    if n == 0:
        return "No more bottles of beer on the wall, no more bottles of beer.\nGo to the store and buy some more, 99 bottles of beer on the wall.\n"
    elif n == 1:
        return "%d bottle of beer on the wall, %d bottle of beer.\nTake it down and pass it around, no more bottles of beer on the wall.\n" % (n, n)
    elif n == 2:
        return "%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottle of beer on the wall.\n" % (n, n, n - 1)
    else:
        return "%d bottles of beer on the wall, %d bottles of beer.\nTake one down and pass it around, %d bottles of beer on the wall.\n" % (n, n, n - 1)
