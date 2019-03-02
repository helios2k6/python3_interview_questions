def th(n, start, aux, dest):
    if n > 0:
        th(n - 1, start, dest, aux)
        dest.append(start.pop())
        th(n - 1, aux, start, dest)

def test1():
    start = [3, 2, 1]
    aux = []
    dest = []
    th(3, start, aux, dest)
    print(start)
    print(aux)
    print(dest)

test1()