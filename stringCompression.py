def createCompressedStr(compressedStr, currentChar, currentCount):
    return f"{compressedStr}{currentChar}{currentCount}"

def stringCompression(inStr):
    compressedStr = ""
    currentChar = None
    currentCount = 0

    for c in inStr:
        if not currentChar:
            currentChar = c
            currentCount = 1
        elif c == currentChar:
            currentCount += 1
        else:
            compressedStr = createCompressedStr(compressedStr, currentChar, currentCount)
            currentChar = c
            currentCount = 1
    # capture last item
    compressedStr = createCompressedStr(compressedStr, currentChar, currentCount)

    return compressedStr if len(inStr) > len(compressedStr) else inStr


examples = {
    "aabccccaa": "a2b1c4a2",
    "a": "a",
    "ababab": "ababab",
    "aaaa": "a4",
}

for k, v in examples.items():
    strCompressed = stringCompression(k)
    if strCompressed != v:
        print(f"Expected {v}. Got {strCompressed}")
