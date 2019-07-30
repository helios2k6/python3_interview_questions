def isSentence(s: str, vocab: dict) -> bool:
    if not s:
        return True

    cache = [False for _ in range(0, len(s) + 1)]
    for i in range(1, len(s) + 1):
        if not cache[i] and s[0:i] in vocab:
            cache[i] = True

        if cache[i]:
            if i == len(s):
                return True

            for j in range(i + 1, len(s) + 1):
                if not cache[j] and s[i:j] in vocab:
                    cache[j] = True
                if j == len(s) and cache[j]:
                    return True
    return False

def testCore(s: str, vocab: dict) -> None:
    print(f"{s} is a sentence: {isSentence(s, vocab)}")

def test0() -> None:
    vocab = {
        "this": True,
        "thisi": True,
        "is": True,
        "facebook": True,
        "face": True,
    }
    testCore("thisisfacebook", vocab)

def test1() -> None:
    testCore("thisisfacebook", {})

test0()
test1()