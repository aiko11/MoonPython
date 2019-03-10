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

# 가장 밑에 있는 함수부터 실행됩니다.
@measure_run_time
@parameter_logger
def worker(delay_time):
    print("%d %s" % (delay_time, "초 후에 실행 됩니다."))
    time.sleep(delay_time)


if __name__ == "__main__":
    worker(5)
