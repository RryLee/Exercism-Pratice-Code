def to_rna(s):
    result = ''
    for l in s:
        if l == 'C':
            result += 'G'
        elif l == 'G':
            result += 'C'
        elif l == 'T':
            result += 'A'
        elif l == 'A':
            result += 'U'
        else:
            result += l

    return result
