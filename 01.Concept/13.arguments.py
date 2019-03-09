
def test(name, *args, **kargs):
    print("========= fixed argument")
    print("Fixed argument : %s" % name)

    print("========= *args argument")
    for arg in args:
        print("Argument : %s" % arg)

    print("========= **args argument")
    for keyword, arg in kargs.items():
        print("Argument keyword : %s, arg : %s" % (keyword, arg))


def main():
    args = ["red", "blue", "first", "second"]
    kargs = {"red":"color", "blue":"color", "first":"number", "second":"number"}

    test("python", *args, **kargs)
    test("php", "red", "blue", "green", red="color", blue="color")


if __name__ == "__main__":
    main()
