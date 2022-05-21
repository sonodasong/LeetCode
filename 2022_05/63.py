from typing import List


class Solution:

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[m - 1][n - 1] == 1: return 0
        d = {(0, 0): 1}
        return self.find(obstacleGrid, d, m - 1, n - 1)

    def find(self, obstacleGrid, d, i, j):
        if (i, j) in d: return d[(i, j)]
        r = 0
        if i - 1 >= 0 and obstacleGrid[i - 1][j] == 0:
            r += self.find(obstacleGrid, d, i - 1, j)
        if j - 1 >= 0 and obstacleGrid[i][j - 1] == 0:
            r += self.find(obstacleGrid, d, i, j - 1)
        d[(i, j)] = r
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.uniquePathsWithObstacles(obstacleGrid=[[0,0,0],[0,1,0],[0,0,0]]))
    print(solution.uniquePathsWithObstacles(obstacleGrid=[[0,1],[0,0]]))
    print(solution.uniquePathsWithObstacles(obstacleGrid=[[0,0],[0,1]]))
