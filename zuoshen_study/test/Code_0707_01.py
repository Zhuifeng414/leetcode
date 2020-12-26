class Solution(object):
    def __init__(self):
        return

    def robot(self, command, obstacles, x, y):
        temp = [0, 0]
        one_cycle = [[0, 0]]
        for elem in command:
            if elem == 'U':
                temp[1] = temp[1] + 1
                one_cycle.append(temp[:])
            else:
                temp[0] = temp[0] + 1
                one_cycle.append(temp[:])
        for elem in obstacles:
            if elem[0] >= x and elem[1] >= y:
                continue
            all_cycle = min(elem[0]//temp[0], elem[1]//temp[1])
            leave = [0, 0]
            leave[0] = elem[0] - all_cycle * temp[0]
            leave[1] = elem[1] - all_cycle * temp[1]
            if leave in one_cycle:
                return False
        all_cycle = min(x//temp[0], y//temp[1])
        leave = [0, 0]
        leave[0] = x - all_cycle * temp[0]
        leave[1] = y - all_cycle * temp[1]
        if leave in one_cycle:
            return True
        else:
            return False


