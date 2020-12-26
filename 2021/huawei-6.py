#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == '__main__':
    cap_list = [int(item) for item in str(sys.stdin.readline().strip()).split(' ')]
    sumk = sum(cap_list)
    n = len(cap_list)
    res = [0 for i in range(n)]
    key_list = []
    key_index = 0
    for i in range(1, 201):
        if ('7' in str(i)) or (i%7 == 0):
            res[i%n - 1] += 1
            key_index += 1
            if key_index >= sumk:
                break

    str_res = [str(item) for item in res]
    print(' '.join(str_res))





