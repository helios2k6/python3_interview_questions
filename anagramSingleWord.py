def generateSubstrings(s: str) -> list:
    substrings = []
    lengthOfS = len(s)
    for i in range(0, lengthOfS):
        for j in range(i + 1, lengthOfS + 1):
            substrings.append(s[i:j])
    return substrings

def isAnagram(a: str, b: str, anagramBag: dict) -> bool:
    if len(a) != len(b):
        return False

    if a in anagramBag and b in anagramBag[a]:
        return True

    aStrCharMap = {}
    bStrCharMap = {}
    for ac in a:
        if ac not in aStrCharMap:
            aStrCharMap[ac] = 0
        aStrCharMap[ac] += 1

    for bc in b:
        if bc not in bStrCharMap:
            bStrCharMap[bc] = 0
        bStrCharMap[bc] += 1

    for ac, acCount in aStrCharMap.items():
        if ac not in bStrCharMap or bStrCharMap[ac] != acCount:
            return False

    if a not in anagramBag:
        anagramBag[a] = {}
    if b not in anagramBag:
        anagramBag[b] = {}
    
    anagramBag[a][b] = True
    anagramBag[b][a] = True
    return True

def numberOfAnagrams(s: str) -> int:
    anagramBagMap = {}
    substrings = generateSubstrings(s)
    anagramCount = 0
    for i in range(0, len(substrings) - 1):
        for j in range(i + 1, len(substrings)):
            if isAnagram(substrings[i], substrings[j], anagramBagMap):
                anagramCount += 1
    return anagramCount

def testCore(s: str) -> None:
    print(f"{numberOfAnagrams(s)}")

def mainTest() -> None:
    strings = [
        "kkkk",
        "ifailuhkqq",
        "ifailuhkqqhucpoltgtyovarjsnrbfpvmupwjjjfiwwhrlkpekxxnebfrwibylcvkfealgonjkzwlyfhhkefuvgndgdnbelgruel",
        "gffryqktmwocejbxfidpjfgrrkpowoxwggxaknmltjcpazgtnakcfcogzatyskqjyorcftwxjrtgayvllutrjxpbzggjxbmxpnde",
        "mqmtjwxaaaxklheghvqcyhaaegtlyntxmoluqlzvuzgkwhkkfpwarkckansgabfclzgnumdrojexnrdunivxqjzfbzsodycnsnmw",
        "ofeqjnqnxwidhbuxxhfwargwkikjqwyghpsygjxyrarcoacwnhxyqlrviikfuiuotifznqmzpjrxycnqktkryutpqvbgbgthfges",
        "zjekimenscyiamnwlpxytkndjsygifmqlqibxxqlauxamfviftquntvkwppxrzuncyenacfivtigvfsadtlytzymuwvpntngkyhw",
    ]

    # Answers:
    # 10
    # 3
    # 399
    # 471
    # 370
    # 403
    # 428
    for s in strings:
        testCore(s)

mainTest()