# -----------------------------------------------
# try문에 else을 사용하는 것과 없는 것에 차이
# -----------------------------------------------

import os
import time

TRY_TEST_FILE = "sample_file_01"
TRY_ELSE_TEST_FILE = "sample_file_02"


def write_file_only_try():
    try:
        f = open(TRY_TEST_FILE,"w")

        for i in range(1000000):
            f.write(str(i))

        f.close()
    except:
        print("File open error")
    finally:
        os.remove(TRY_TEST_FILE)


def write_file_try_else():
    try:
        f = open(TRY_ELSE_TEST_FILE,"w")
    except:
        print("File open error")
    else:
        for i in range(1000000):
            f.write(str(i))

        f.close()
    finally:
        os.remove(TRY_ELSE_TEST_FILE)


def check_runtime(func):
    accumulate_time = 0
    for i in range(10):
        start = time.time()
        func()
        accumulate_time += (time.time() - start)
    print("Run time summary : %s"  % str(accumulate_time / 10))


if __name__ == "__main__":
    print("========== try Performance Test")
    check_runtime(write_file_only_try)

    print("========== try/else Performance Test")
    check_runtime(write_file_try_else)
