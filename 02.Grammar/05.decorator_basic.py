# ---------------------------------------------------------------
# 파이썬에서 지원하는 데코레이터 입니다.
# 사용법은 함수나 클래스를 인자로 받는 클로저를 정의하고 그 안에 기능을 구현합니다.
# 다음으로 데코레이터를 사용하는 함수나 클래스의 선언 바로 윗줄에 키워드를 사용해서
# 위에서 정의한 클로저의 이름을 적어주면 됩니다.
# ---------------------------------------------------------------

def deco(func):
    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper

@deco
def base():
    print("base function")
    return 99

if __name__ == "__main__":
    print("=============== Run decorator")
    result = base()

    print("result: %s" % str(result))

