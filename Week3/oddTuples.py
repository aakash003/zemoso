def oddTuples(aTup):
    tup =()
    ln = len(aTup)
    for i in range(0,ln):
        if i%2 == 0 :
            tup = tup + (aTup[i],)
    return tup
