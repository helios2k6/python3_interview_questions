def findOptimalSplits(dims: list) -> list:
    n = len(dims) - 1 
    costs = [[0 for _ in dims] for _ in dims]
    splits = [[0 for _ in dims] for _ in dims]
    for subSequenceLength in range(1, n):
        for startOfRangeIndex in range(0, n - subSequenceLength):
            endOfRangeIndex = startOfRangeIndex + subSequenceLength
            costs[startOfRangeIndex][endOfRangeIndex] = None
            for splitIndex in range(startOfRangeIndex, endOfRangeIndex):
                localCost = costs[startOfRangeIndex][splitIndex] + costs[splitIndex + 1][endOfRangeIndex] + (dims[startOfRangeIndex - 1] * dims[splitIndex] * dims[endOfRangeIndex])
                if not costs[startOfRangeIndex][endOfRangeIndex] or localCost < costs[startOfRangeIndex][endOfRangeIndex]:
                    costs[startOfRangeIndex][endOfRangeIndex] = localCost
                    splits[startOfRangeIndex][endOfRangeIndex] = splitIndex
    return splits[0]

def testCore(dims: list) -> None:
    print(f"Optimal Splits Matrix: {findOptimalSplits(dims)}")

def test0() -> None:
    testCore([10000, 100, 100, 1000])

test0()