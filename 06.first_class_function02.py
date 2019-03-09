# --------------------------------------------------------------------------------------------
# First-Class Function Citizen(일급 객체) 속성을 가진다는 것은
# 어떤 객체를 다른 개체으 매개변수로 전달하거나, 함수의 반환값으로 사용하거나,
# 변수에 값으로 할당할 수 있다는 것을 의미합니다.
# 여기서 '개체'라는 것은 자료형이 될 수도 있고, 함수가 될 수도 잇고, 클래스가 될 수도 잇습니다.
# --------------------------------------------------------------------------------------------


def square(x):
    return x * x


def bind(func, arg_list):
    result = []
    for arg in arg_list:
        result.append(func(arg))
    return result


def main():
    arg_list = [5, 10]
    print("Assign variable & send parameter")
    sequares = bind(square, arg_list)
    print(sequares)


if __name__ == "__main__":
    main()
