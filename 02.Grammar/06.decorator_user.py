def deco(func):
    def wrapper():
        print("before")
        ret = func()
        print("after")
        return ret

    return wrapper

def base():
    print("base function")


if __name__ == "__main__":
    print("=============== Run decorator")

    # f = deco(base)
    # f()
    #위 코드를 한 줄로 작업

    deco(base)()
