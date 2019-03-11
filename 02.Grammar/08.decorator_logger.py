# ----------------------------------------------------------------
# 다중 decorator 적용시
# ----------------------------------------------------------------


import time
import datetime

def measure_run_time(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end  = time.time()

        print("%s, function running time : %s" % (func.__name__, end-start))
        return result

    return wrapper


def parameter_logger(func):

    def wrapper(*args, **kwargs):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
        print("[%s] args : %s, kwargs : %s" % (timestamp, args, kwargs))
        return func(*args, **kwargs)

    return wrapper


# 함수의 선언과 가까이 있는 것 즉, 가장 밑에 있는 함수부터 실행됩니다.
# pramerter_logger이 먼저 실행되고 measure_run_time이 실행됩니다.
# 첫번째 pramerter_logger은 5라는 인자가 정상적으로 출력이 되었습니다.
# measure_run_time도 정상적으로 출력은 되었지만 함수명이 worker가 아니라 wrapper 입니다.

@measure_run_time
@parameter_logger
def worker(delay_time):
    print("%d %s" % (delay_time, "초 후에 실행 됩니다."))
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
