class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        for i in range(len(customers)):
            if grumpy[i] == 0:
                grumpy[i] = customers[i]
            else:
                grumpy[i] = 0
        all_sum = sum(customers[:X])
        sub_sum = sum(grumpy[:X])
        max_res = all_sum - sub_sum
        for i in range(len(customers) - X):
            all_sum = all_sum - customers[i] + customers[i + X]
            sub_sum = sub_sum - grumpy[i] + grumpy[i + X]
            max_res = max(max_res, all_sum - sub_sum)
        return sum(grumpy) + max_res
