# ----------------------------------------------------------------
# 클래스로 데코레이터를 만들게 되면 데코레이터로 만들 클래스에
# __call__ 메서드를 정의하고 로직을 작성하면 됩니다.
출력 결과물은 함수로 만든 데코레이터와 똑같습니다.
하지만 함수로 만든 것과 다른 부분이 2가지가 있습니다.
첫 번째는 __call__메서드가 클로저로 되어 있지 않습니다.
두 번째는 wraps 데코레이터를 사용하지 않았습니다.
# ----------------------------------------------------------------

import time
from functools import update_wrapper

class MeasureRuntime:

    def __init__(self, f):
        self.func = f
        update_wrapper(self, self.func)

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.func(*args, **kwargs)
        end = time.time()
        print("'%s' function running time : %s" % (self.func.__name__, end-start))

        return result

@MeasureRuntime
def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
