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
    n = int(sys.stdin.readline().strip())
    while n > 0:
        print(find_max_bottle(n))
        n = int(sys.stdin.readline().strip())


