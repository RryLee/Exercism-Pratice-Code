def slices(num, limit):
    if len(num) < limit or limit == 0:
        raise ValueError

    results = []

    for i in range(len(num) - limit + 1):
        results.append(map(int, list(num[i:i + limit])))

    return results
