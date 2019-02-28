def solvePuzzleImpl(currentPoint, rows, cols, forbiddenSpots, seenSpots):
    seenSpots[currentPoint] = True
    x, y = currentPoint
    if y == (rows - 1) and x == (cols - 1):
        return [currentPoint]

    pointToRight = (x + 1, y)
    if x + 1 < cols and not pointToRight in forbiddenSpots and not pointToRight in seenSpots:
        # we can go right
        rightResult = solvePuzzleImpl(pointToRight, rows, cols, forbiddenSpots, seenSpots)
        if rightResult:
            return [currentPoint] + rightResult

    pointToBottom = (x, y + 1)
    if y + 1 < rows and not pointToBottom in forbiddenSpots and not pointToBottom in seenSpots:
        bottomResult = solvePuzzleImpl(pointToBottom, rows, cols, forbiddenSpots, seenSpots)
        if bottomResult:
            return [currentPoint] + bottomResult

    return None


def solvePuzzle(rows, cols, forbiddenSpots):
    return solvePuzzleImpl((0, 0), rows, cols, forbiddenSpots, {})