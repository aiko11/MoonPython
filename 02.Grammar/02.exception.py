# ----------------------------------------------------
# 파이썬에서 예외처리시 특별한 점이 하나 있습니다.
# try / except(catch) / else /finally 에서 else라는 구문이 추가 되어 있습니다.
# 기능적으로 try에 작성하는 코드와 else에 작성하는 코드의 차이는 없습니다.
# 하지만 효율성에 차이가 나는데 try에 작성하는 코드는 예외를 감시하는 내부 프로세스를
# 거치기 때문에 else문에 작성된 코드보다 실행 속도가 떨어집니다.
# ----------------------------------------------------

EXIST_FILE = "sample_file"
NON_EXIST_FILE = "non_exist_sample_file"

def read_file(file_name):
    try:
        f = open(file_name, "r")
    except:
        print("File open error")
    else:
        print(f.read())
        f.close()
    finally:
        print("End file read\n\n")

if __name__ == "__main__":
    print("============== Exist file open")
    read_file(EXIST_FILE)

    print("============= Non-Exists file open")
    read_file(NON_EXIST_FILE)

