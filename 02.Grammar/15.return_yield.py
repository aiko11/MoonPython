# ---------------------------------------------------------------------------
# generator 는 간단하게 설명하면 iterator 를 생성해 주는 function 이다.
# iterator 는 next() 메소드를 이용해 데이터에 순차적으로 접근이 가능한 object 이다.
# ---------------------------------------------------------------------------
# Generator 함수는 함수 안에 yield 를 사용하여 데이타를 하나씩 리턴하는 함수이다.
# Generator 함수가 처음 호출되면, 그 함수 실행 중 처음으로 만나는 yield 에서 값을 리턴한다.
# Generator 함수가 다시 호출되면, 직전에 실행되었던 yield 문 다음부터
# 다음 yield 문을 만날 때까지 문장들을 실행하게 된다.
# 이러한 Generator 함수를 변수에 할당하면 그 변수는 generator 클래스 객체가 된다.
# ---------------------------------------------------------------------------
# 리스트나 Set과 같은 컬렉션에 대한 iterator는 해당 컬렉션이 이미 모든 값을 가지고 있는 경우이나,
# Generator는 모든 데이타를 갖지 않은 상태에서 yield에 의해 하나씩만 데이타를 만들어 가져온다는 차이점이 있다.
# 이러한 Generator는 데이타가 무제한이어서 모든 데이타를 리턴할 수 없는 경우나,
# 데이타가 대량이어서 일부씩 처리하는 것이 필요한 경우, 혹은 모든 데이타를 미리 계산하면
# 속도가 느려서 그때 그때 On Demand로 처리하는 것이 좋은 경우 등에 종종 사용된다.
# ---------------------------------------------------------------------------
# 아래 예제에서는
# gen function 출력에서 에러 발생
# normal function in loop 출력에서 에러 발생
# ---------------------------------------------------------------------------

# Generator 함수
def gen():
    yield 1
    yield 2
    yield 3

def normal():
    return 1
    return 2
    return 3

def main():
    print("======= gen function")
    print(gen())    # error 발생

    print("======= normal function")
    print(normal())

    print("======= gen function in loop")
    for g in gen():
        print(g)

    print("======= normal function in loop")
    for n in normal():
        print(n)    # error 발생


if __name__=="__main__":
    main()