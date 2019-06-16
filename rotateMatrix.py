class SquareMatrix:
    def __init__(self, length: int) -> None:
        self.length = length
        self.coordToValueMap = {}

    def setValue(self, row, col, value) -> None:
        if row not in self.coordToValueMap:
            self.coordToValueMap[row] = {}
        self.coordToValueMap[row][col] = value

    def getValue(self, row, col) -> int:
        if row in self.coordToValueMap and col in self.coordToValueMap[row]:
            return self.coordToValueMap[row][col]
        return 0

    def __str__(self) -> str:
        strings = []
        for row in range(0, self.length):
            for col in range(0, self.length):
                strings.append(self.getValue(row, col).__str__())
                strings.append(", ")
            strings.append("\n")
        return "".join(strings)

def projectCoordinate(row, col, length) -> (int, int):
    return (length - 1 - col, row)

def rotateMat(matrix: SquareMatrix) -> None:
    rings = matrix.length // 2
    for ring in range(0, rings):
        for relativeSideValue in range(0, matrix.length - ring - 1):
            topCoordinate = (ring, ring + relativeSideValue)
            rightCoordinate = (ring + relativeSideValue, matrix.length - ring - 1)
            bottomCoordinate = (matrix.length - ring - 1, matrix.length - ring - 1 - relativeSideValue)
            leftCoordinate = (matrix.length - ring - 1 - relativeSideValue, ring)

            # Save top for now
            tempValue = matrix.getValue(topCoordinate[0], topCoordinate[1])

            # Override top with left coordinate
            matrix.setValue(topCoordinate[0], topCoordinate[1], matrix.getValue(leftCoordinate[0], leftCoordinate[1]))

            # Override left coordinate with bottom coordinate
            matrix.setValue(leftCoordinate[0], leftCoordinate[1], matrix.getValue(bottomCoordinate[0], bottomCoordinate[1]))

            # Override bottom coordinate with right coordinate
            matrix.setValue(bottomCoordinate[0], bottomCoordinate[1], matrix.getValue(rightCoordinate[0], rightCoordinate[1]))

            # Override right coordinate with temp
            matrix.setValue(rightCoordinate[0], rightCoordinate[1], tempValue)

def testCase0() -> None:
    testCase = SquareMatrix(3)
    testCase.setValue(0, 0, 1)
    testCase.setValue(0, 1, 2)
    testCase.setValue(0, 2, 3)

    testCase.setValue(1, 0, 4)
    testCase.setValue(1, 1, 5)
    testCase.setValue(1, 2, 6)

    testCase.setValue(2, 0, 7)
    testCase.setValue(2, 1, 8)
    testCase.setValue(2, 2, 9)

    print(testCase)
    rotateMat(testCase)
    print(testCase)

testCase0()