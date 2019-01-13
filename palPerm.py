import copy

def freqMap(inStr):
    map = {}
    spaceMap = []
    index = 0
    for c in inStr:
        if c.isalpha():
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        elif c.isspace():
            spaceMap.append(index)
        index += 1
    return map, spaceMap

def isValidFreqMap(inFreqMap):
    totalCount = 0
    for c, i in inFreqMap.items():
        totalCount += i

    if totalCount % 2 == 0:
        for c, i in inFreqMap.items():
            if i % 2 != 0:
                return False
    else:
        numOddNumbers = 0
        for c, i in inFreqMap.items():
            if i % 2 != 0:
                numOddNumbers += 1
        return numOddNumbers <= 1
    return True

def genPalPerms(strFreqMap):
    if not strFreqMap:
        return []

    if len(strFreqMap) == 1:
        for c, i in strFreqMap.items():
            if i == 1:
                return [c]
            else:
                return []

    allSubPerms = []
    for c, i in strFreqMap.items():
        if i > 1:
            copyOfFreqMap = copy.deepcopy(strFreqMap)
            copyOfFreqMap[c] -= 2
            if copyOfFreqMap[c] == 0:
                copyOfFreqMap.pop(c, None)
            subPerm = genPalPerms(copyOfFreqMap)
            for perm in subPerm:
                allSubPerms.append(f"{c}{perm}{c}")
    
    return allSubPerms

def generatePalendromPerm(inStr):
    strFreqMap, spaceMap = freqMap(inStr)
    if not isValidFreqMap(strFreqMap):
        print("Not a valid frequency map")
        return []

    palPermWithoutSpaces = genPalPerms(strFreqMap)

    palPermWithSpaces = []
    for pal in palPermWithoutSpaces:
        for spaceIndex in spaceMap:
            left = pal[:spaceIndex]
            right = pal[spaceIndex:]
            newPal = f"{left} {right}"
            palPermWithSpaces.append(newPal)
    return palPermWithSpaces

testString = "taco cat"

generatedPerms = generatePalendromPerm(testString)

print(generatedPerms)