def deco(func):
    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper

def base():
    print("base function")
    return 100


if __name__ == "__main__":
    print("=============== Run decorator")

    # f = deco(base)
    # result = f()
    # 아래 코드는 위 코드를 한 줄로 작업

    result = deco(base)()


    print("result: %s" % str(result))
