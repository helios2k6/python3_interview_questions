def maxAlternatingSubsetSum(arr: list) -> int:
    if not arr:
        raise Exception("Cannot have empty array")
    if len(arr) == 1:
        return arr[0]
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]

    cache = [0 for _ in range(0, len(arr))]
    cache[0] = arr[0]
    cache[1] = arr[1]
    for i in range(2, len(arr)):
        previousLargestValue = cache[i - 2]
        previousLargestValue2 = cache[max(i - 3, 0)]
        cache[i] = max(previousLargestValue, previousLargestValue2, previousLargestValue + arr[i], previousLargestValue2 + arr[i], arr[i])

    return cache[-1] if cache[-1] > cache[-2] else cache[-2]

def testCore(arr: list) -> None:
    print(f"Max sum: {maxAlternatingSubsetSum(arr)}")

def test0() -> None:
    # Should be 8
    testCore([-2, 1, 3, -4, 5])

def test1() -> None:
    testCore([3, 7, 4, 6, 5])

def test2() -> None:
    testCore([2, 1, 5, 8, 4])

def test3() -> None:
    testCore([3, 5, -7, 8, 10])

test0()
test1()
test2()
test3()