def findEnd(a):
    i = 0
    for e in a:
        if not e:
            return i
        i += 1
    return i

def shiftElements(a, i, e):
    lenOfA = len(a)
    if lenOfA <= i or e >= lenOfA:
        return
    for m in reversed(range(i + 1, e + 1)):
        a[m] = a[m-1]

def mergeSorted(a, b):
    endOfA = findEnd(a)
    aIter = 0
    bIter = 0
    lenOfB = len(b)
    while (bIter < lenOfB):
        if aIter >= endOfA:
            a[aIter] = b[bIter]
            aIter += 1
            bIter += 1
            endOfA += 1
        else:
            aE = a[aIter]
            bE = b[bIter]
            if bE < aE:
                shiftElements(a, aIter, endOfA)
                a[aIter] = bE
                aIter += 1
                bIter += 1
                endOfA += 1
            else:
                aIter += 1

def test1():
    a = [1, 3, 4, None, None]
    b = [2, 5]
    mergeSorted(a, b)
    print(a)

def test2():
    a = [1, None, None]
    b = [-1, 0]
    mergeSorted(a, b)
    print(a)

test1()
test2()