from typing import List


class Solution:

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return self.find(k, n, 1)

    def find(self, k, n, a):
        if k == 1: return [[n]]
        l = []
        for i in range(a, 9):
            if n - i < i + 1: continue
            t = max(10 - k, i)
            if n - i > (t + 10) * (9 - t) // 2: continue
            if k - 1 > 9 - i: continue
            for t in self.find(k - 1, n - i, i + 1):
                l.append([i] + t)
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.combinationSum3(k=3, n=7))
    print(solution.combinationSum3(k=3, n=9))
    print(solution.combinationSum3(k=4, n=1))
    print(solution.combinationSum3(k=2, n=18))
