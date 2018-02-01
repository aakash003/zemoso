def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    str1 = 'abcdefghijklmnopqrstuvwxyz'
    list1 = list(str1)
    str2=''
    b=set(lettersGuessed)
    for i in str1:
        if i not in b:
            str2 = str2 + i
    return str2
