# ----------------------------------------------------------------
# 클래스로 데코레이터를 만들것을 27라인에 있는 @MeasureRuntime 지우고
# 만들어 보겠습니다.
__init__은 생성자로 사용됩니다.
__call__은 클래스를 함수처럼 사용할 때 호출됩니다.
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

def worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    f = MeasureRuntime(worker)
    f(5)