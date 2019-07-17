def isSentenceImpl(s: str, vocab: dict, cache: dict) -> bool:
    if s in cache:
        return cache[s]
    if not s:
        return False
    if s in vocab:
        cache[s] = True
        return True
    else:
        cache[s] = False

    # go through each 
    for i in range(0, len(s) - 1):
        for j in range(i + 1, len(s)):
            head = s[i:j]
            tail = s[j:]
            cache[head] = isSentenceImpl(head, vocab, cache)
            cache[tail] = isSentenceImpl(tail, vocab, cache)
            if cache[head] and cache[tail]:
                return True

    return False

def isSentence(s: str, vocab: dict) -> bool:
    return isSentenceImpl(s, vocab, {})

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