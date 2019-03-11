# ----------------------------------------------------------------
# 08.decorator_logger.py 실행시 문제점에 대해 파악하기위해서
# decorator을 풀어서 확인하는 작업
# 42라인에서 measure_run_time 함수로 인자를 넣는 것이
# worker이 아니라 parameter_logger의 반환값이기 때문입니다.
# 이 문제를 해결하기 위해서 @wraps함수를 사용합니다.
# ----------------------------------------------------------------

import time
import datetime
from functools import wraps


def measure_run_time(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()

        print("%s, function running time : %s" % (func.__name__, end-start))
        return result

    return wrapper


def parameter_logger(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
        print("[%s] args : %s, kwargs : %s" % (timestamp, args, kwargs))
        return func(*args, **kwargs)

    return wrapper


@measure_run_time
@parameter_logger
def worker(delay_time):
    print("%d %s" % (delay_time, "초 후에 실행 됩니다."))
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
