import sys
if __name__ == "__main__":
    #读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    res = [int(item) for item in line.split()]
    #print(n, res)
    res.sort()
    # print('res', res)
    #res = [1, 2, 3, 4, 5]
    p = 0 #小
    q = len(res) - 1 #大
    all_res = 0
    flag = 0
    while p < q:
        #print(p, q)
        v_minus = res[q] - res[p]
        if flag == 1:
            flag += 1
        for h in range(p+1, q):
            #print(res[p], res[h], res[q])
            if res[h] > v_minus:
                if res[h] + res[p] > res[q]:
                    all_res += 1

        if flag == 0:
            p += 1
            flag += 1

        if flag == 2:
            q -= 1
            flag = 0

    print(all_res)






