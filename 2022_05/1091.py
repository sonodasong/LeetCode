from typing import List
from queue import PriorityQueue


class Solution:

    # def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
    #     n = len(grid)
    #     c = [[False] * n for _ in range(n)]
    #     r = [[None] * n for _ in range(n)]
    #     if grid[0][0] == 1: return -1
    #     q = PriorityQueue()
    #     q.put((1, (0, 0)))
    #     while q.qsize() > 0:
    #         a, (i, j) = q.get(False)
    #         c[i][j] = True
    #         r[i][j] = a
    #         for i, j in self.adjcant(grid, c, n, i, j):
    #             t = r[i][j]
    #             if t is None or a + 1 < t:
    #                 r[i][j] = a + 1
    #                 q.put((a + 1, (i, j)))
    #     return r[-1][-1] if c[-1][-1] else -1

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = [[False] * n for _ in range(n)]
        if grid[0][0] == 1: return -1
        l = [(0, 0)]
        c[0][0] = True
        d = 0
        while len(l) > 0:
            d += 1
            t = []
            for i, j in l:
                if i == n - 1 and j == n - 1: return d
                a = self.adjcant(grid, c, n, i, j)
                for x, y in a:
                    c[x][y] = True
                t += a
            l = t
        return d if c[-1][-1] else -1

    def adjcant(self, grid, c, n, i, j):
        l = []
        for a in [-1, 0, 1]:
            a += i
            if a < 0: continue
            if a >= n: continue
            for b in [-1, 0, 1]:
                b += j
                if b < 0: continue
                if b >= n: continue
                if c[a][b]: continue
                if grid[a][b] == 1: continue
                l.append((a, b))
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPathBinaryMatrix(grid=[[0,1],[1,0]]))
    print(solution.shortestPathBinaryMatrix(grid=[[0,0,0],[1,1,0],[1,1,0]]))
    print(solution.shortestPathBinaryMatrix(grid=[[1,0,0],[1,1,0],[1,1,0]]))
