def poker(hands):
    return allmax(hands, key=hand_rank)

def allmax(iterable, key = None):
    key = key or (lambda x: x)
    return [item for item in iterable if card_ranks(item) == card_ranks(max(iterable, key = key))]

def hand_rank(hand):
    ranks = card_ranks(hand)
    groups = [(ranks.count(i), i) for i in set(ranks)]
    groups.sort(reverse=True)
    counts, number = zip(*groups)
    staright = (len(counts) == 5) and (max(number) - min(number) == 4)
    flush = len(set([s for r, s in hand])) == 1
    return (8 if staright and flush else
            7 if counts == (4, 1) else
            6 if counts == (3, 2) else
            5 if flush else
            4 if staright else
            3 if counts == (3, 1, 1) else
            2 if counts == (2, 2, 1) else
            1 if counts == (2, 1, 1, 1) else
            0, number)

def card_ranks(hand):
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks
