import sys
def find_max_bottle(init_n):
    max_bottle = 0
    while init_n >= 3:
        sub_bottle = init_n // 3
        init_n = init_n % 3 + sub_bottle
        max_bottle += sub_bottle
    if init_n == 2:
        max_bottle += 1
    return max_bottle


if __name__ == "__main__":
    #读取第一行的n

    input_str = sys.stdin.readline().strip()
    res = []
    while input_str:
        input_n = int(input_str)
        deal_set = set()
        for i in range(input_n):
            num = int(sys.stdin.readline().strip())
            deal_set.add(num)
        sub_res = list(deal_set)
        sub_res.sort()
        res += sub_res
        input_str = sys.stdin.readline().strip()
    for item in res:
        print(item)




