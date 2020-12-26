class Hanoi:
    def __init__(self):
        return

    def hanoi(self, n):
        if n > 0:
            self.func(n, n, 'left', 'mid', 'right')


    def func(self, rest, down, left, mid, right):
        if rest == 1:
            print('move ' + str(down) + ' left ' + str(left) + ' to ' + str(right))
        else:
            self.func(rest-1, down-1, left, right, mid)
            self.func(1, down, left, mid, right)
            self.func(rest-1, down-1, mid, left, right)
        return

if __name__ == '__main__':
    n = 3
    Hanoi().hanoi(3)