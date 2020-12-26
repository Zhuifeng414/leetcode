class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        if len(asteroids) < 2:
            return asteroids
        p = 0
        q = 1
        stack = []
        res = [i for i in asteroids]
        while q < len(asteroids):
            if asteroids[p] > 0 and asteroids[q] < 0:
                if asteroids[p] + asteroids[q] > 0: # q remove
                    res[q] = 'inf'
                    q = q + 1
                elif asteroids[p] + asteroids[q] < 0: # p remove
                    res[p] = 'inf'
                    if len(stack) > 0:
                        p = stack.pop(-1)
                    else:
                        p = q + 1
                        q = q + 2
                else: # remove p, q
                    res[p] = 'inf'
                    res[q] = 'inf'
                    if len(stack) > 0:
                        p = stack.pop(-1)
                        q = q + 1
                    else:
                        p = q + 1
                        q = q + 2
            else:
                stack.append(p)
                p = q
                q = q + 1
        return [item for item in res if item != 'inf']




if __name__ == '__main__':
    asteroids = [-2,1,-1,-2]
    res = Solution().asteroidCollision(asteroids)
    print(res)
