def processWordImpl(dictionary, word, currentChainLength):
    wordLength = len(word)
    if wordLength == 1:
        return currentChainLength

    currentMaxChainLength = currentChainLength
    for i in range(0, wordLength):
        h = word[0:i]
        t = word[i+1::]
        newString = h + t
        if newString in dictionary:
            localChainLength = processWordImpl(dictionary, newString, currentChainLength + 1)
            if localChainLength > currentMaxChainLength:
                currentMaxChainLength = localChainLength
    return currentMaxChainLength

def processWord(dictionary, word):
    return processWordImpl(dictionary, word, 1)

def longestChain(words):
    currentMax = 1
    for word in words:
        localMax = processWord(words, word)
        if localMax > currentMax:
            currentMax = localMax
    return currentMax

def test1():
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestChain(words))
test1()