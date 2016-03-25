def largest_product(string, n):
    length = len(string)
    max = 0
    i = 0
    while i < length - n:
        current = 1
        j = i
        while j < i + length:
            current *= int(string[j])
        if current > max:
            max = current
    return max
