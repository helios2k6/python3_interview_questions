def sortStack(stack:list):
    stackLen = len(stack)
    if not stack or stackLen == 1:
        return stack

    tempStack = []
    watermark = 0
    while watermark < stackLen:
        cursor = 0
        largestElem = None
        while cursor < (stackLen - watermark):
            e = stack.pop()
            if not largestElem:
                largestElem = e
            elif largestElem < e:
                tempStack.append(largestElem)
                largestElem = e
            else:
                tempStack.append(e)
            cursor += 1

        stack.append(largestElem)
        watermark += 1

        while tempStack:
            stack.append(tempStack.pop())

testStack = [3, 4, 1, 5, 1, 7, 8, 2, 0]

sortStack(testStack)

print(testStack)