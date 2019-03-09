
def normal_func():
    pass


def nested_func():

    def inner():
        pass

    p = dir(inner())

    print("=== inner attribute ===")
    print(p)


def closure():
    x = 10
    z = 30

    def inner():
        y = 20
        return x+y+z

    p = dir(inner())

    print("=== inner attribute ===")
    print(p)
    return inner


if __name__ == "__main__":
    p1 = dir(normal_func())
    p2 = dir(nested_func())
    p3 = dir(closure())
    p4 = closure()

    print("=== attribute ===")
    print(p1)
    print(p2)
    print(p3)
    print(len(p4.__closure__))
    print(p4.__closure__[0].cell_contents)
    print(p4.__closure__[1].cell_contents)
