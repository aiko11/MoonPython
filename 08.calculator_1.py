# --------------------------------------------------------------------------------------------
# Nested function(중첩함수)는 함수로 감싸인 함수를 뜻합니다.
# 내부 함수들은 scope chain에 의해서 자신을 감싸고 있는 외부 함수의 메모리에 접근이 가능합니다.
# 즉, 외부 함수의 변수나 매개변수 등에 접근할 수 있습니다.
# --------------------------------------------------------------------------------------------


def calculator(x, y):
    def add():
        return x + y

    def sub():
        return x - y

    return (add(), sub())


# 함수를 리턴해 준다.
def calculator2(x):
    def add(y):
        return x + y

    return add


if __name__ == "__main__":
    print("=== print calculation ===")
    print(calculator(10, 5))

    f = calculator2(100)
    print(f(99))
    print(f(25))
