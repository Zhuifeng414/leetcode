class Solution(object):
    def bestTeamScore(self, scores, ages):
        """
        :type scores: List[int]
        :type ages: List[int]
        :rtype: int
        """
        age_score = [[ages[i], scores[i]] for i in range(len(scores))]
        age_score.sort(key=lambda x: (x[0], x[1]))
        dp = [age_score[i][1] for i in range(len(ages))]
        res = 0
        for i in range(len(scores)):
            for j in range(i):
                if (age_score[j][1] <= age_score[i][1]) or (age_score[j][0] == age_score[i][0]):
                    dp[i] = max(dp[i], dp[j] + age_score[i][1])
            res = max(res, dp[i])
        return res

    def bestTeamScore_ans(self, scores, ages):
            players = sorted(zip(ages, scores))  # 从小到大排序
            n = len(players)
            dp = [players[i][1] for i in range(n)]  # 选中第i个球员时最大的分数总和
            for i in range(n):
                ceil_age, ceil_score = players[i]
                for j in range(i):  # 对每一个年龄小等于player_i的球员
                    age, score = players[j]
                    if ceil_age == age or ceil_score >= score:  # 将选中player_i, 基于dp[j]状态转移
                        dp[i] = max(dp[i], ceil_score + dp[j])
            return max(dp)


if __name__ == '__main__':
    scores = [1, 3, 5, 10, 15]
    ages = [1, 2, 3, 4, 5]
    print('my:  ', Solution().bestTeamScore(scores, ages))
    print('ans: ', Solution().bestTeamScore_ans(scores, ages))

