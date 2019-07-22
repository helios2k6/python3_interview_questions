import random

EPSILON = 0.001
MAX_CANDIDATES = 300
MAX_CANDIDATE_DIFFERENCE = 0.25

def generateRandomMatrix(n: int, maxCandidates) -> list:
    return [[random.random() for _ in range(0, n)] for _ in range(0, maxCandidates)]

def areCandidatesCloseEnough(candidates: list) -> bool:
    largestDifference = None
    for i in range(1, len(candidates) - 1):
        localDifference = candidates[i - 1] - candidates[i]
        if not largestDifference or localDifference > largestDifference:
            largestDifference = localDifference
    return largestDifference < MAX_CANDIDATE_DIFFERENCE

def selectRandomNumbers(randomMatrix: list) -> list:
    for i in range(0, len(randomMatrix)):
        if areCandidatesCloseEnough(randomMatrix[i]):
            return randomMatrix[i]
    return None

def normalizeNumbers(randomNumbers: list) -> list:
    ratio = sum(randomNumbers)
    return [n / ratio for n in randomNumbers]

def generateRandomAmounts(n: int, cap: int) -> list:
    randomNumbers = None
    while not randomNumbers:
        randomNumbers = selectRandomNumbers(generateRandomMatrix(n, MAX_CANDIDATES))
    randomNumbers = normalizeNumbers(randomNumbers)

    amounts = []
    for i in randomNumbers:
        amounts.append(round(i * cap, 2))
    return amounts

def testCore(n: int, cap: int) -> None:
    amounts = generateRandomAmounts(n, cap)
    generatedAmountsRunningSum = 0
    for a in amounts:
        generatedAmountsRunningSum += a
    if abs(generatedAmountsRunningSum - cap) > EPSILON:
        print(f"Generated amounts exceed epsilon of {EPSILON}")
    else:
        print(f"Amounts: {amounts}")

def test0() -> None:
    testCore(3, 75)

test0()
