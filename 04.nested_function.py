# --------------------------------------------------------------------------------------------
# global 키워드만 있으면 파이썬의 변수 선언 방식으로 인한 문제는 모두 해결 될까요?
# 아직 하나 더 남았습니다. 바로 nonlocal 키워드 입니다.
# 아래 예제는 함수안에 함수가 선언되어 있는 형태인데, 이런 것을 nested function 이라고 부릅니다.
# 13번째 줄 nonlocal 키워드를 지우면 global 선언 했을 때 처럼 에러가 생깁니다.
# 정의 되지 않은 함수를 실행한다고..
# --------------------------------------------------------------------------------------------


def greeting(name):
    greeting_msg = "heelo "

    def add_name():
        # nonlocal은 python3부터 지원함
        nonlocal greeting_msg

        greeting_msg += " ^^ "
        return ("%s%s" % (greeting_msg, name))

    msg = add_name()
    print(msg)

if __name__=="__main__":
    greeting("python")