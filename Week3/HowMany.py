def how_many(aDict):
    res = 0
    for i in aDict.values():
        res += len(i)
    return res
