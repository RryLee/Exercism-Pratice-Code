def distance(a, b):
    # return len([letter for letter in range(len(a)) if a[letter] != b[letter]])
    return len([(i, j) for i, j in zip(a, b) if i != j])
