# ------------------------------------------------
# 전역변수을 함수내에서 접근 가능하게 하는 global 키워드
# ------------------------------------------------

msg = "hello"

def write():
    global msg
    msg += " World"
    print(msg)

def main():
    print("=== print msg ===")
    print(msg)

    print("=== write function ===")
    write()

    print("=== print msg ===")
    print(msg)


if __name__=="__main__":
    main()