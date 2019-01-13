import copy

def freqMap(inStr):
    map = {}
    for c in inStr:
        if c in map:
            map[c] += 1
        else:
            map[c] = 1
    return map

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
    strFreqMap = freqMap(inStr)
    if not isValidFreqMap(strFreqMap):
        print("Not a valid frequency map")
        return []
    return genPalPerms(strFreqMap)

testString = "tacocat"

generatedPerms = generatePalendromPerm(testString)

print(generatedPerms)