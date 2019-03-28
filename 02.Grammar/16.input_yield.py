# ---------------------------------------------------------------------------
# gen2함수는 yield를 값을 입력하는 것과 반환하는 것 2가지 목적으로 사용하는 예입니다.
# 값이 먼저 반환되고 입력받는 값을 다시 value에 할당합니다.
# ---------------------------------------------------------------------------

def gen():
    value = 2

    while True:
        print(value)
        value = yield


def gen2():
    value = 1

    while True:
        value = yield value


def main():
    print("========= gen function")
    g = gen()

    next(g)
    g.send(3)
    g.send(5)


def main2():
    print("========= gen2 function")
    g = gen2()

    print(next(g))
    print(g.send(2))
    print(g.send(10))
    print(g.send(5))
    print(next(g))


if __name__=="__main__":
    main2()
