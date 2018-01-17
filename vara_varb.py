if type (varA) == str or type (varB) == str:
    print ("string involved")
elif type (varA) == int or float and type (varB) == int or float:
    if varA > varB:
        print ("bigger")
    if varA == varB:
        print ("equal")
    if varA < varB:
        print ("smaller")