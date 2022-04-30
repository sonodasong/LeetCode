from typing import List
from queue import PriorityQueue


class Solution:

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        r = len(heights);
        c = len(heights[0])
        checked = [[None] * c for _ in range(r)]
        self.h = heights; self.r = r; self.c = c; self.checked = checked

        q = PriorityQueue()
        q.put((0, (0, 0)))
        while not q.empty():
            d, (i, j) = q.get()
            if checked[i][j] is not None: continue
            checked[i][j] = d
            t = self.find(i, j)
            if len(t) == 0: continue
            for x, y in t:
                q.put((max(self.d(i, j, x, y), checked[i][j]), (x, y)))
        return checked[r - 1][c - 1]

    def d(self, i, j, x, y):
        h = self.h
        return abs(h[i][j] - h[x][y])

    def find(self, i, j):
        c = self.checked
        l = []
        if i + 1 < self.r and c[i + 1][j] is None:
            l.append((i + 1, j))
        if i - 1 >= 0 and c[i - 1][j] is None:
            l.append((i - 1, j))
        if j + 1 < self.c and c[i][j + 1] is None:
            l.append((i, j + 1))
        if j - 1 >= 0 and c[i][j - 1] is None:
            l.append((i, j - 1))
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumEffortPath(heights=[[1,2,2],[3,8,2],[5,3,5]]))
    print(solution.minimumEffortPath(heights=[[1,2,3],[3,8,4],[5,3,5]]))
    print(solution.minimumEffortPath(heights=[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))
