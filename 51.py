from typing import List


class Solution:

    def solveNQueens(self, n: int) -> List[List[str]]:
        c = set(); l = set(); r = set()
        a = self.find(n, 0, c, l, r)
        return [self.get(n, l) for l in a]

    def find(self, n, i, c, l, r):
        a = []
        for j in range(n):
            if j in c: continue
            if i + j in l: continue
            if i - j in r: continue
            if i == n - 1:
                a.append([j])
            else:
                cc = c.copy(); ll = l.copy(); rr = r.copy()
                cc.add(j); ll.add(i + j); rr.add(i - j)
                for t in self.find(n, i + 1, cc, ll, rr):
                    a.append([j] + t)
        return a

    def get(self, n, l):
        r = [['.'] * n for _ in range(n)]
        for i, j in enumerate(l):
            r[i][j] = 'Q'
        r = [''.join(r) for r in r]
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.solveNQueens(n=4))
    print(solution.solveNQueens(n=1))
