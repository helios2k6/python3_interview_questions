def processWord(dictionary, word, currentChainLength, memoPad):
    wordLength = len(word)
    if wordLength == 1:
        return currentChainLength

    if word in memoPad:
        return memoPad[word]

    currentMaxChainLength = currentChainLength
    for i in range(0, wordLength):
        h = word[0:i]
        t = word[i+1::]
        newString = h + t
        if newString in dictionary:
            localChainLength = processWord(dictionary, newString, currentChainLength + 1, memoPad)
            if localChainLength > currentMaxChainLength:
                currentMaxChainLength = localChainLength
    
    return currentMaxChainLength

def longestChain(words):
    currentMax = 1
    wordsAsDictionary = {}
    for word in words:
        wordsAsDictionary[word] = True
    
    memoPad = {}
    for word in words:
        localMax = 1
        if word in memoPad:
            localMax = memoPad[word]
        else:
            localMax = processWord(wordsAsDictionary, word, 1, memoPad)
        if localMax > currentMax:
            currentMax = localMax
    return currentMax

def test0():
    words = ["a", "b", "ba", "bca"]
    print(longestChain(words))

def test1():
    words = ["a", "b", "ba", "bca", "bda", "bdca"]
    print(longestChain(words))

def test2():
    words = [
        "a",
        "zxb",
        "ba",
        "bca",
        "bda",
        "bdca",
        "zxbe",
        "azxbe",
        "azxpbe"
    ]

    print(longestChain(words))

test0()
test1()
test2()