from typing import List


class Solution:

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.matrix = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.d = [[None] * self.n for _ in range(self.m)]
        r = 0
        for i in range(self.m):
            for j in range(self.n):
                t = self.find(i, j)
                if t > r:
                    r = t
        return r

    def find(self, i, j):
        t = self.d[i][j]
        if t is not None: return t
        l = [0]
        if self.check(i, j, i - 1, j):
            l.append(self.find(i - 1, j))
        if self.check(i, j, i + 1, j):
            l.append(self.find(i + 1, j))
        if self.check(i, j, i, j - 1):
            l.append(self.find(i, j - 1))
        if self.check(i, j, i, j + 1):
            l.append(self.find(i, j + 1))
        t = max(l) + 1
        self.d[i][j] = t
        return t

    def check(self, x, y, i, j):
        if i < 0: return False
        if i >= self.m: return False
        if j < 0: return False
        if j >= self.n: return False
        if self.matrix[i][j] <= self.matrix[x][y]: return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestIncreasingPath(matrix=[[9,9,4],[6,6,8],[2,1,1]]))
    print(solution.longestIncreasingPath(matrix=[[3,4,5],[3,2,6],[2,2,1]]))
    print(solution.longestIncreasingPath(matrix=[[1]]))
