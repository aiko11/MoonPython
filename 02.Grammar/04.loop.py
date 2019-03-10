# ----------------------------------------------------------
# python2 에서는 range, xrange 함수 둘 다 사용할 수 있으나
# python3 에서는 xrange 사라졌습니다.
# ----------------------------------------------------------
import sys

def get_type_and_size(value):
    print("type : %s" % type(value))
    print("size : %s" % sys.getsizeof(value))


def main():
    print("==================== Range size 10, 100")
    get_type_and_size(range(10))
    get_type_and_size(range(100))

    print("==================== Xrange size 10, 100")
    # get_type_and_size(xrange(10))
    # get_type_and_size(xrange(100))

if __name__ == "__main__":
    main()

