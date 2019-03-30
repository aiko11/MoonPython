# ---------------------------------------------------------------------------
# 예제는 매개변수로 받은 iterms의 값을 하나씩 반환하는 예제입니다.
# item 을 반환할 때 마다 지역변수로 선언한 count의 값을 증가시킵니다.
# 그러다 count 값이 10이 되면 return으로 -1이 반환되며 제너레이터가 종료됩니다.
# 그리고 리턴값 -1은 출력되지 않았고 오류도 발생하지 않습니다.
# 반복문에서 제너레이터를 수행하다 return으로 값을 받으면 StopIteration 예외가
# 발생하며 멈추게 됩니다. 그래서 반환값도 오류도 생기지 않은 것입니다.
# ---------------------------------------------------------------------------

def gen(items):
    count=0

    for item in items:
        if count == 10:
            return -1

        count += 1
        yield item

if __name__=="__main__":
    print("========= gen")

    # x=5 이면 0,1,2,3,4 출력
    x=15
    for i in gen(range(x)):
        print(i)