def intervals(percents: list) -> list[tuple[int, int]]:
    arr = []
    inf = 0
    sup = 0
    for i, ii in enumerate(percents):
        if i != len(percents)-1: sup += ii
        else: sup += ii + 0.0000000000000001
        if i != 0: inf += percents[i-1]
        arr.append((inf, sup))
    
    return arr