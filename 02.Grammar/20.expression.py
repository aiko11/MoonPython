# ----------------------------------------------------------
# Generator Expression과 같은 역활을 합니다.
# 사용 방법은 동일하지만 문법은 조금 다릅니다.
# comprehension(컴프리헨션)에서는 []나 {}를 사용했지만
# generator exprssion은 ()를 사용합니다.
# ----------------------------------------------------------

SAMPLE_LIST = [1, 2, 3, 4, 5]

def generate_sample_list():
    result = (x*x for x in SAMPLE_LIST)
    print(result)
    print("~~~~~~~~~~~~")
    return result

def generate_list_by_range():
    result = (i for i in range(10))
    print(result)
    print("~~~~~~~~~~~~")
    return result

def print_generator(items):
    for item in items:
        print(item)

def main():
    print("========== list")
    print_generator(generate_sample_list())
    print_generator(generate_list_by_range())


if __name__ == '__main__':
    main()
