# --------------------------------------------------------------------------------------------
# 클로저에서 외부 함수의 변수들 즉, nonlocal 변수들은 외부 함수가 실행되는 시점에 생성되고,
# 복사되어 내부 함수의 __closure__ 속성에 저장됩니다.
# 그래서 nonlocal 변수로 시간과 관련된 값을 사용하게 되면 의도하지 않은 결과가 나올 수 있습니다.
# 예제를 통해서 출력결과를 확인하세요.
# --------------------------------------------------------------------------------------------


import datetime
import time

def logger():
    now = datetime.datetime.now()

    def print_log(msg):
        return("[%s] %s" % (now, msg))

    return print_log


def main():
    log = logger()
    print(log("start"))

    time.sleep(10)

    print(log("After 10 sec"))


if __name__ == "__main__":
    main()