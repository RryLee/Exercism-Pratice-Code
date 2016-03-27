def parse_binary(numstr):
    if any(x not in '01' for x in numstr):
        raise ValueError("Invalid num string")

    return int(numstr, 2)
