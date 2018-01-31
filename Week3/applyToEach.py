def applyToEach(L, f):
    for i in range(len(L)):
        if i%2 != 0 :
            L[i] = f(L[i])


def oddNeg(a):
    return -a
    
applyToEach(testList,oddNeg)
