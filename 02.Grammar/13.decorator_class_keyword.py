# ----------------------------------------------------------------
# python에서 지원하는 @ kewword를 사용이 필요한 경우 입니다.
# 테코레이터에 매개변수가 있는 경우에는 클러저의 형태를 구현해야 합니다.
# ----------------------------------------------------------------

import time
from functools import wraps

class MeasureRuntime:

    def __init__(self, active_state):
        self.measure_active=active_state

    def __call__(self, func):

        @wraps(func)
        def wrapper(*args, ** kwargs):
            if self.measure_active is False:
                return func(*args, **kwargs)

            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print("'%s' function running time : %s" % (func.__name__, end-start))

            return result

        return wrapper

@MeasureRuntime(True)
def active_worker(delay_time):
    time.sleep(delay_time)

@MeasureRuntime(False)
def non_active_worker(delay_time):
    time.sleep(delay_time)


if __name__ == "__main__":
    active_worker(5)
    non_active_worker(5)