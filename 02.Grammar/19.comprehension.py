# --------------------------------------------------------------------------
# Comprehension 이란 iterable한 오브젝트를 생성하기 위한 방법중 하나로
# 파이썬에서 사용할 수 있는 유용한 기능중 하나입니다.
# 파이썬에는 다음과 같은 크게 네 가지 종류의 Comprehension 이 있다.
# - List Comprehension (LC)
# - Set Comprehension (SC)
# - Dict Comprehension (DC)
# - Generator Expression (GE)
# Generator 의 경우 comprehension 과 형태는 동일하지만 특별히 expression 이라고 부른다.
# --------------------------------------------------------------------------

v_list = [1,2,3]
v_dict_key = ["korea","japen", "china"]
v_dict_value =[82, 81, 90]

def print_list_with_comprehension():
    v_list_comprehension = [x*x for x in v_list]
    print (v_list_comprehension)

def print_list_with_for():
    result = []

    for v in v_list:
        result.append(v)
    print(result)


def print_dict_with_comprehension():
    v_dict_comprehension = {k:v for k, v in zip(v_dict_key, v_dict_value)}
    print(v_dict_comprehension)


def print_dict_with_for():
    result = {}
    for k, v in zip(v_dict_key, v_dict_value):
        result[k] =  v
    print(result)

def main():
    print("=========== list")
    print(v_list)
    print_list_with_comprehension()
    print_list_with_for()

    print("========== dict")
    print(v_dict_key)
    print(v_dict_value)
    print_dict_with_comprehension()
    print_dict_with_for()

if __name__ == '__main__':
    main()