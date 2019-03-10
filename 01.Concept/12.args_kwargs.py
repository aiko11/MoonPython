# --------------------------------------------------------------------------------------------
# 매개변수  *args는 key값이 없는 리스트이고, (non-keyworded)
# 매개변수 **args는 key값이 있는 사전이 온다고 생각하면 됩니다. (keyworded)
# --------------------------------------------------------------------------------------------

def args_test(*args):
    print("=== args list ===")
    for arg in args:
        print("Argument : %s" % arg)

def kwargs_test(**args):

    print("=== kwargs list ===")

    for keyword, arg in args.items():
        print("Argument keyword : %s, arg : %s" % (keyword, arg))


def main():
    args = ["red","blue", "first", "second"]
    args2 = {"red":"color", "blue":"color", "first":"11111", "second":"999"}

    args_test(*args)
    kwargs_test(**args2)


if __name__ == "__main__":
    main()

