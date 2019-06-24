class CharacterBag:
    def __init__(self, string: str):
        self.characterBag = {}
        self.memoizedSizeOfCharacterBag = None
        for char in string:
            if char not in self.characterBag:
                self.characterBag[char] = 0
            self.characterBag[char] += 1

    def size(self) -> int:
        if self.memoizedSizeOfCharacterBag:
            return self.memoizedSizeOfCharacterBag

        self.memoizedSizeOfCharacterBag = 0
        for numChars in self.characterBag.values():
            self.memoizedSizeOfCharacterBag += numChars

        return self.memoizedSizeOfCharacterBag

    def isEqual(self, other: "CharacterBag") -> bool:
        if self.size() != other.size():
            return False
        for char, numChars in self.characterBag.items():
            if char not in other.characterBag or other.characterBag[char] != numChars:
                return False
        return True

def generateSubstringMap(s: str) -> dict:
    substrings = {}
    lengthOfS = len(s)
    for i in range(0, lengthOfS):
        for j in range(i + 1, lengthOfS + 1):
            substring = s[i:j]
            if substring not in substrings:
                substrings[substring] = 0
            substrings[substring] += 1
    return substrings

def projectCharacterBagToCountList(substringMap: dict) -> list:
    characterBagList = []
    for substring, substringCount in substringMap.items():
        characterBag = CharacterBag(substring)
        for i in range(0, substringCount):
            characterBagList.append(characterBag)
    return characterBagList

def bucketCharacterBagList(characterBagList: list) -> dict:
    buckets = {}
    for characterBag in characterBagList:
        sizeOfBag = characterBag.size()
        if sizeOfBag not in buckets:
            buckets[sizeOfBag] = []
        buckets[sizeOfBag].append(characterBag)
    return buckets

def numberOfAnagrams(s: str) -> int:
    bucketsOfCharacterBagLists = bucketCharacterBagList(projectCharacterBagToCountList(generateSubstringMap(s)))
    anagramCount = 0
    for listOfBags in bucketsOfCharacterBagLists.values():
        numberOfCharacterBags = len(listOfBags)
        for i in range(0, numberOfCharacterBags - 1):
            for j in range(i + 1, numberOfCharacterBags):
                if listOfBags[i].isEqual(listOfBags[j]):
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