from typing import List


class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        c = set(coins)
        d = {}
        t = self.find(c, d, amount)
        if t is None:
            t = -1
        return t

    def find(self, c, d, a):
        if a in d: return d[a]
        if a in c:
            d[a] = 1
            return 1
        l = []
        for x in c:
            if x > a: continue
            t = self.find(c, d, a - x)
            if t is None: continue
            l.append(t + 1)
        if len(l) == 0:
            d[a] = None
            return None
        d[a] = min(l)
        return d[a]


if __name__ == '__main__':
    solution = Solution()
    print(solution.coinChange(coins=[1,2,5], amount=11))
    print(solution.coinChange(coins=[2], amount=3))
    print(solution.coinChange(coins=[1], amount=0))
