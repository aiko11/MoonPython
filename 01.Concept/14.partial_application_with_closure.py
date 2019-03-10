# --------------------------------------------------------------------------------------------
# 파이썬 내장 모듈을 이용한 Partial 함수와 
# 직접 사용자 함수로 만든 partial_make 함수
# --------------------------------------------------------------------------------------------
from functools import partial


def partial_make(func, *a_args):

    def wrapper(*b_args):
        args = list(a_args)
        args.extend(b_args)

        return func(*args)

    return wrapper

def logging(year, month, day, title, content):
    print("%s-%s-%s %s:%s" % (year,month, day, title, content))

def main():
    print("------------------ use logging function")
    logging("2019","03","09","python2", "End of support in 2020")
    logging("2019","03","09","python3", "Updateing")

    print("------------------ use partial_make function")
    f = partial_make(logging, "2019","03", "10")
    f("python2", "End of support in 2020")
    f("python3", "Updateing")

    print("------------------ use partial of python function")
    k = partial(logging, "2019", "03", "10")
    k("python2", "End of support in 2020")
    k("python3", "Updateing")

if __name__ == "__main__":
    main()
