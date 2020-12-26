#coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys
def str_bfs(root_str):
    print('now: ', root_str)
    if root_str == '{}':
        return ''
    if '{' not in root_str:
        return root_str
    head = root_str[0]
    pos, neg = 0, 0
    new_root_str = root_str[2:-1]
    if ',' not in new_root_str:
        left, right = new_root_str, ''
    else:
        i = 0
        for i in range(len(new_root_str)):
            item = new_root_str[i]
            if item == '{':
                pos += 1
            if item == '}':
                neg += 1
            if item == ',' and pos == neg:
                break
        if i == len(new_root_str)-1:
            left, right = new_root_str, ''
        else:
            left = new_root_str[:i]
            right = new_root_str[i+1:]
    print('head:', head, 'left:', left, 'right:', right)
    return str_bfs(left) + head + str_bfs(right)

if __name__ == '__main__':
    # a{b{d,e{g,h{,i}}},c{f}}
    # dbgehiafc
    # init_str = 'a{b{d,e{g,h{,i}}},c{f}}'

    # a{c{e}}

    init_str = str(sys.stdin.readline().strip())
    while init_str:
        print(str_bfs(init_str))
        init_str = str(sys.stdin.readline().strip())






