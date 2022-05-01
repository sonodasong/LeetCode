from typing import List
# from bisect import insort, bisect_left


class Solution:

    # def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
    #     l = set()
    #     dr = {}
    #     dc = {}
    #     for x, y in walls:
    #         l.add((x, y))
    #         if x in dr:
    #             insort(dr[x], y)
    #         else:
    #             dr[x] = [-1, y, n]
    #         if y in dc:
    #             insort(dc[y], x)
    #         else:
    #             dc[y] = [-1, x, m]
    #     for x, y in guards:
    #         l.add((x, y))
    #         if x in dr:
    #             t = dr[x]
    #             i = bisect_left(t, y)
    #             a = t[i - 1] + 1; b = t[i]
    #             for i in range(a, b):
    #                 l.add((x, i))
    #             insort(t, y)
    #         else:
    #             for i in range(n):
    #                 l.add((x, i))
    #             dr[x] = [-1, y, n]
    #         if y in dc:
    #             t = dc[y]
    #             i = bisect_left(t, x)
    #             a = t[i - 1] + 1; b = t[i]
    #             if b > a:
    #                 for i in range(a, b):
    #                     l.add((i, y))
    #             insort(t, x)
    #         else:
    #             for i in range(m):
    #                 l.add((i, y))
    #             dc[y] = [-1, x, m]
    #     return m * n - len(l)

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        l = [[True] * n for _ in range(m)]
        for x, y in guards:
            l[x][y] = 'g'
        for x, y in walls:
            l[x][y] = 'w'
        for i in range(m):
            state = 0
            prev = None
            for j in range(n):
                t = l[i][j]
                if t == 'w':
                    if prev is not None:
                        for k in range(state, j):
                            l[i][k] = False
                    state = j + 1
                    prev = None
                elif t == 'g':
                    for k in range(state, j):
                        l[i][k] = False
                    state = j + 1
                    prev = 0
            if prev is not None:
                for k in range(state, n):
                    l[i][k] = False
        for j in range(n):
            state = 0
            prev = None
            for i in range(m):
                t = l[i][j]
                if t == 'w':
                    if prev is not None:
                        for k in range(state, i):
                            l[k][j] = False
                    state = i + 1
                    prev = None
                elif t == 'g':
                    for k in range(state, i):
                        l[k][j] = False
                    state = i + 1
                    prev = 0
            if prev is not None:
                for k in range(state, m):
                    l[k][j] = False
        a = 0
        for i in range(m):
            for j in range(n):
                if l[i][j] == True:
                    a += 1
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.countUnguarded(m=4, n=6, guards=[[0,0],[1,1],[2,3]], walls=[[0,1],[2,2],[1,4]]))
    print(solution.countUnguarded(m=3, n=3, guards=[[1,1]], walls=[[0,1],[1,0],[2,1],[1,2]]))
