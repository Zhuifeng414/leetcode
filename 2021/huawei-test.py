def num2name(input_num):
    str_num_dict = {
        1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G',
        8: 'H', 9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N',
        15: 'O', 16: 'P', 17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U',
        22: 'V', 23: 'W', 24: 'Z', 25: 'Y', 26: 'Z', 0: 'Z'
    }
    if input_num <= 0 or type(input_num) != type(10):
        print('Error! Please check input.')
        return -1
    state = []
    while input_num > 26:
        state.append(input_num % 26)
        if input_num % 26 == 0:
            input_num = input_num // 26 - 1
        else:
            input_num = input_num // 26
    #print(state, input_num)
    res = ''
    res += str_num_dict[input_num]
    for item in state[::-1]:
        res += str_num_dict[item]
    return res

if __name__ == '__main__':
    check_dict = {
        26: 'Z',
        27: 'AA',
        28: 'AB',
        52: 'AZ',
        53: 'BA',
        54: 'BB',
        104: 'CZ',
        105: 'DA',
        26*26-1: 'YY',
        26*26: 'YZ',
        26*26+1: 'ZA',
        702: ''
    }
    for key_item in check_dict.keys():
        if check_dict[key_item] == num2name(key_item):
            print('right:', key_item, num2name(key_item))
            continue
        else:
            print('error!', key_item, ' ans:', check_dict[key_item], '   yours:', num2name(key_item))
    print('finished!')
