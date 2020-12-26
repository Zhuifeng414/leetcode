import sys
def string_class(all_string):
    class_dict = {}
    for item in res:
        item_len = len(item)
        if item_len in class_dict.keys():
            class_dict[item_len].append(item)
        else:
            class_dict[item_len] = [item]
    return class_dict

def type_num(str_list):
    sub_res = 0
    i = 0
    if len(str_list) <= 1:
        return 0
    #for i in range(len(str_list)):
    while i < len(str_list):
        flag = 0
        for j in range(len(str_list[i])):
            rever_str = str_list[i][j:] + str_list[i][:j]
            if rever_str in str_list[:i] + str_list[i+1:]:
                if flag == 0:
                    sub_res += 1
                    flag = 1
                str_list.remove(rever_str)
        i += 1
    return sub_res


if __name__ == "__main__":
    #读取第一行的n
    n = int(sys.stdin.readline().strip())
    res = []
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = line.split()[0]
        res.append(values)

    #res = ['ab', 'ba', 'abc', 'bca', 'e']

    class_dict = string_class(res)
    all_sum = 0
    for class_item in class_dict.keys():
        sub_list = class_dict[class_item]
        all_sum += type_num(sub_list)
    print(all_sum)

