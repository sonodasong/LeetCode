from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        c = set(); l = set(); r = set()
        return self.find(n, 0, c, l, r)

    def find(self, n, i, c, l, r):
        a = 0
        for j in range(n):
            if j in c: continue
            if i + j in l: continue
            if i - j in r: continue
            if i == n - 1:
                a += 1
            else:
                cc = c.copy(); ll = l.copy(); rr = r.copy()
                cc.add(j); ll.add(i + j); rr.add(i - j)
                a += self.find(n, i + 1, cc, ll, rr)
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(n=4))
    print(solution.solveNQueens(n=1))
    print(solution.solveNQueens(n=9))
