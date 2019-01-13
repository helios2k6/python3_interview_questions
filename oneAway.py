def isOneAway(a, b, editOccured):
    if not a:
        if not b:
            return True
        elif len(b) == 1 and not editOccured:
            return True
        else:
            return False
    if not b:
        if not a:
            return True
        elif len(a) == 1 and not editOccured:
            return True
        else:
            return False
    
    ac = a[0]
    aTail = a[1:]
    
    bc = b[0]
    bTail = b[1:]

    if ac == bc:
        return isOneAway(aTail, bTail, editOccured)
    else:
        if editOccured:
            return False
        else:
            aLen = len(a)
            bLen = len(b)
            if aLen == bLen:
                return isOneAway(aTail, bTail, True)
            elif aLen > bLen:
                return isOneAway(aTail, b, True)
            else:
                return isOneAway(a, bTail, True)

def isOneAwayIter(a, b):
    aLen = len(a)
    bLen = len(b)

    if abs(aLen - bLen) > 1:
        return False
    
    if aLen == bLen:
        ai = 0
        bi = 0

        didEdit = False
        while ai < aLen and bi < bLen:
            if a[ai] != b[bi]:
                if didEdit:
                    return False
                didEdit = True
            ai += 1
            bi += 1
        return True
    else:
        ai = 0
        bi = 0

        while ai < aLen and bi < bLen:
            if a[ai] != b[bi]:
                if abs(ai - bi) == 1:
                    return False
                else:
                    if aLen > bLen:
                        ai += 1
                    else:
                        bi += 1
            else:
                ai += 1
                bi += 1
        return True

examples = [
    ("pale", "ple", True),
    ("pales", "pale", True),
    ("pale", "bale", True),
    ("pale", "bake", False),
]

for a, b, r in examples:
    resultRec = isOneAway(a, b, False)
    resultIter = isOneAwayIter(a, b)
    if r != resultRec:
        print(f"Unexpected result (rec) of {resultRec} for {a} vs {b}")

    if r != resultIter:
        print(f"Unexpected result (iter) of {resultIter} for {a} vs {b}")

print("Finished checking examples")