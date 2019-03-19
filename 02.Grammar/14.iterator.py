# -------------------------------------------------------------------------------------
# iterator는 값을 순차적으로 반복해서 하나씩 반환할 수 있는 개체입니다.
# 비슷한 개념으로 iterable가 있는 보통 이 둘 간의 관계를 많이 혼동 합니다.
# iterable는 가지고 있는 값을 한번에 하나씩 반환할 수 있는 개체입니다.
# 여기서 주의할 점은 한번에 하나씩 반환할 수 있다는 것이지, 한 번에 하나씩 반환해야 한다는 것은 아닙니다.
# 한번에 모든 값을 반환할 수도 있고 한 번에 하나씩만 반환할 수도 있습니다.
# iterable의 예로는 container
# (list, 스트링, 튜플 같은 sequence 타입의 자료형이나 사전같은 non-sequence 타입의 자료형)나
# open files, open sockes 같은 것이 있습니다.
# 내장 함수 iter()는 iter(iterable객체)와 같이 사용하여 iterator를 리턴 합니다.
# -------------------------------------------------------------------------------------
# iterator도 값을 한 번에 하나씩만 반환하는 개체라고 정의했습니다.
# iterator도 iterable처럼 여러개의 값을 가지고 있습니다.
# 그런데 한 번에 하나씩 값을 반환하려면 현재 어디까지 반환했는지 상태를 알고 있어야 합니다.
# 즉, interable과는 달리 iterator는 가지고 있느 값 중에서 이미 반환한 상태를 갖고 있고
# 어디서부터 반환해야 할지 상태를 갖고 있습니다. 그리고 파이썬의 내장 함수인 next를 통해서
# 값을 순차적으로 반환합니다.
# 이 2가지 특성을 이터레이터의 정의라고 생각하면 됩니다.
# -------------------------------------------------------------------------------------


def main():
    # -----------------------------------------
    # 맨 마지막 프린트에서 에러가 발생합니다.
    # 리스트가 이터레이터가 아니라는 오류입니다.
    # -----------------------------------------
    x = [1, 2, 3]
    y = {"red": 1, "blue": 2, "green": 3}

    x_iterator = iter(x)
    y_iterator = iter(y)

    print("================= print type")
    print("list type : %s" % type(x))
    print("dictonary type : %s" % type(y))
    print("list iterator  type : %s" % type(x_iterator))
    print("dictonary iterator type : %s" % type(y_iterator))

    print("================= print next")
    print("list iterator next : %s" % next(x_iterator))
    print("dictonary iterator next : %s" % next(y_iterator))
    print("list next : %s" % next(x))
    print("dictonary next : %s" % next(y))


def main1():
    # -----------------------------------------
    # 순차 적으로 가져오다가 가져올 수 있는 값이 없으면
    # StopIteration 예외를 발생 시킵니다.
    # -----------------------------------------
    x = [1, 2, 3]
    x_iterator = iter(x)

    print("======== print iterator")
    print(next(x_iterator))
    print(next(x_iterator))

    print(next(x_iterator))
    print(next(x_iterator))


def main2():
    # -----------------------------------------
    # for 문에서는 내부적으로 StopIteration 예외에
    # 대한 처리가 되어 있습니다.
    # -----------------------------------------
    x = [1, 2, 3]
    x_iterator = iter(x)

    for a in x_iterator:
        print(a)


if __name__ == "__main__":
    main2()
