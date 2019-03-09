# --------------------------------------------------------------------------------------------
# Higher-Order Function은 first-class function과 유사한 개념으로 고차 함수라고 주로 표현됩니다.
# 함수가 매개변수로 전달되거나, 함수를 반환값으로 사용할 때 higher-order function이라고 하는데
# 둘 중 하나만 성립해도 higher-order function입니다.
# --------------------------------------------------------------------------------------------

LOWER_LIST = ["python", "python2", "python3"]
UPPER_LIST = []

def convert():
    for data in LOWER_LIST:
        UPPER_LIST.append(data.upper())

def main():
    print ("=== print result ===")
    convert()
    print (LOWER_LIST)
    print (UPPER_LIST)


def convert2(data):
    return data.upper()

def main2():
    print("=== print result ===")
    UPPER_LIST = map(convert2, LOWER_LIST) # map은 내장 함수로 첫 번째 매개변수는 함수고 두 번째는 매개변수임.
    print(LOWER_LIST)
    print(list(UPPER_LIST))


if __name__ == "__main__":
    main()
    main2()
