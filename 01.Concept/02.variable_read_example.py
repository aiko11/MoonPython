# --------------------------------------------------------------------------------------------
# Scope
# 파이썬에서 변수의 유효 범위를 계산할 때 네임스페이스(namespace)를 기반으로 계산합니다.
# 어떤  변수가 사용됐다면 네임스페이스를 확인해서 사용된 변수가 네임스페이스에 있는지 확인합니다.

# 파이썬의 네임스페이스는 built-in, global, enclosed, local로 나눌 수 있습니다.
# built-in : 파이썬에 내장되어 있는 네임스페이스로 어디에서나 사용가능 가능합니다.
# global   : 전역적으로 사용이 가능한 네임스페이스로 파일 단위의 모듈 안에서 유효합니다.
#            또 특정 모듈을 import하는 경유 import하는 경우 import한 모듈의 global 변수도 사용이 가능합니다.
# enclosed : 함수 안에 함수가 있는 구조, 즉 외부 함수가 있고, 내부 함수가 있는 구조에서 내부 함수가 외부 함수의 변수에
#            접근할 수 있는 것을 의미합니다.
# local    : 지역적인 네임스페이스로 클래스나 함수의 내부로 한정됩니다.
# --------------------------------------------------------------------------------------------


msg = "hello"


def read_work():
    print(msg)
    print("world")


def read_exception():
    # print(msg)  # 이곳에 주석을 제거하면 지역변수로 인식해서 변수 선언보다 먼저 수행됐다고 판단해서 오류남
    msg = "World"
    print(msg)


def main():
    print("=== first read ===")
    read_work()

    print("=== second read ===");
    read_exception()


if __name__ == "__main__":
    main()
