import sys

def get_hex_value(hex_str):
    hex_dict = {
        '0':0, '1':1, '2':2, '3':3, '4':4,
        '5':5, '6':6, '7':7, '8':8, '9':9,
        'a':10, 'A':10, 'b':11, 'B':11, 'c':12, 'C':12,
        'd':13, 'D':13, 'e':14, 'E':14, 'f':15, 'F':15
    }
    content = hex_str[2:]
    n = len(content)
    #print(content, n)
    res = 0
    for i in range(n):
        #print(content[i], hex_dict[content[i]] * (16**(n-1-i)))
        res += hex_dict[content[i]] * (16**(n-1-i))
    return res

if __name__ == "__main__":
    #读取第一行的n

    input_str = sys.stdin.readline().strip()

    while input_str:
        print(get_hex_value(input_str))
        input_str = sys.stdin.readline().strip()




