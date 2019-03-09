# --------------------------------------------------------------------------------------------
# 클로저(Closure)는 함수의 반환값으로 내부 함수를 사용하는 함수라고 정의할 수 있다.
# --------------------------------------------------------------------------------------------


def multiple_of_ten():
    square_root = 10

    def square(x):
        return square_root ** x;

    return square


def main():
    print("=== print result ===")
    f = multiple_of_ten()

    print(f(2))
    print(f(3))


if __name__ == "__main__":
    main()
