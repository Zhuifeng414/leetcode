class Solution(object):
    def __init__(self):
        return

    def process(self, arr, skip_step, index):
        if index == len(arr)-1:
            return skip_step
        if index > len(arr)-1:
            return -1
        step_res = []
        for i in range(1, arr[index]+1):
            sub_res = self.process(arr, skip_step+1, index+i)
            if sub_res > 0:
                step_res.append(sub_res)
        return min(step_res)

    def jump(self, arr):
        if len(arr) == 0:
            return 0
        jump = 0
        cur = 0
        next = 0
        for i in range(len(arr)):
            if cur < i:
                jump += 1
                cur = next
            next = max(next, i+arr[i])
        return jump

if __name__ == '__main__':
    arr = [3, 2, 3, 1, 1, 4]
    res = Solution().process(arr, 0, 0)
    print(res)