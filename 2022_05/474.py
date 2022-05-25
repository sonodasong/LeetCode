from typing import List


class Solution:

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        d = {}
        for s in strs:
            s = self.c(s)
            if s in d:
                d[s] += 1
            else:
                d[s] = 1
        l = [(*k, v) for k, v in d.items()]
        return self.find(l, 0, m, n)

    def find(self, l, k, m, n):
        if m < 0: return None
        if n < 0: return None
        r = []
        for i in range(k, len(l)):
            a, b, c = l[i]
            for j in range(1, c + 1):
                t = self.find(l, i + 1, m - a * j, n - b * j)
                if t is None: continue
                r.append(j + t)
        return 0 if len(r) == 0 else max(r)

    def c(self, s):
        n = len(s)
        a = sum([1 for c in s if c == '0'])
        return (a, n - a)


# class Solution:

#     def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#         # Knapsack problem with two constrains, m and n
#         # we start in reverse to avoid same combo 
#         dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
#         for subset in strs:
#             zeros = subset.count('0')
#             ones = len(subset) - zeros
#             for i in range(m, zeros - 1, -1):
#                 for j in range(n, ones - 1, -1):
#                     dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
#         return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.findMaxForm(strs=['10','0001','111001','1','0'], m=5, n=3))
    print(solution.findMaxForm(strs=['10','0','1'], m=1, n=1))
    print(solution.findMaxForm(strs=['10','0001','111001','1','0'], m=4, n=3))
