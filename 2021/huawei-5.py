#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    cap_list = [int(item) for item in str(sys.stdin.readline().strip()).split(' ')]
    min_cap = int(sys.stdin.readline().strip())
    #print(n, cap_list, min_cap)
    cap_list.sort()
    res = 0
    p, q = 0, len(cap_list)-1
    while p < q:
        if cap_list[q] >= min_cap:
            res += 1
            print('q', q, cap_list[q])
            q -= 1

        else:
            while (cap_list[q] + cap_list[p] < min_cap) and (p < q):
                p += 1
            if p < q and cap_list[q] + cap_list[p] >= min_cap:
                res += 1
                #print('pq', p, q, cap_list[q], cap_list[p])
                p += 1
                q -= 1

    if (p == q) and cap_list[p] >= min_cap:
        res += 1
        #print('p', cap_list[p])
    print(res)

