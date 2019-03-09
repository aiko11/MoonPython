# --------------------------------------------------------------------------------------------
# python2에서는 사전 안에 있는 key 값을 찾을 때는 has_key와 in 이라는 내장 함수를 사용했습니다.
# python3에서는 in만 사용할 수 있습니다.
# --------------------------------------------------------------------------------------------

def main():
    dic = {"korea":82, "japen":81}

    # print ("==== has key ===")
    # print (dic.has_key("korea"))
    # print (dic.has_key("china"))

    print ("=== in ===")
    print ("korea" in dic)
    print ("china" in dic)

if __name__ == "__main__":
    main()