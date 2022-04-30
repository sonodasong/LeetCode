from typing import List, Optional


# class Solution:

#     def minCostConnectPoints(self, points: List[List[int]]) -> int:
#         points = list(set([(x, y) for x, y in points]))
#         p = points[0]
#         x, y = p
#         b = [x + y, x + y, y - x, y - x]
#         c = [p]
#         u = points[1:]
#         dis = 0
#         while len(u) > 0:
#             uu = u.copy()
#             p, d = self.e(b, c, uu)
#             bb = self.b(b, *p)
#             # t = [self.c(bb, x, y) for x, y in u]
#             # while True in t:
#             #     p, d = self.e(b, c, uu, p)
#             #     bb = self.b(b, *p)
#             #     t = [self.c(bb, x, y) for x, y in u]
#             c.append(p)
#             u.remove(p)
#             b = bb
#             dis += d
#         return dis

#     def d(self, x, y, a, b):
#         return abs(x - a) + abs(y - b)

#     def d0(self, b, x, y):
#         x0 = (b[0] - b[2]) // 2; y0 = (b[0] + b[2]) // 2
#         x1 = (b[0] - b[3]) // 2; y1 = (b[0] + b[3]) // 2
#         x2 = (b[1] - b[2]) // 2; y2 = (b[1] + b[2]) // 2
#         x3 = (b[1] - b[3]) // 2; y3 = (b[1] + b[3]) // 2
#         m = (self.d(x, y, x0, y0), self.d(x, y, x1, y1), self.d(x, y, x2, y2), self.d(x, y, x3, y3))
#         return min(m), max(m)

#     def e(self, b, c, u, e=None):
#         if e is not None:
#             u.remove(e)
#         m = [self.d0(b, x, y) for x, y in u]
#         t = min([t for _, t in m])
#         m = [i for i, (mi, _) in enumerate(m) if mi <= t]
#         dm = [self.d2(c, *u[i]) for i in m]
#         t = min(dm)
#         return u[m[dm.index(t)]], t

#     def c(self, b, x, y):
#         u = x + y
#         v = y - x
#         return (u > b[0]) and (u < b[1]) and (v > b[2]) and (v < b[3])

#     def d2(self, c, x, y):
#         return min([abs(x - x0) + abs(y - y0) for x0, y0 in c])

#     def b(self, b, x, y):
#         u = x + y
#         v = y - x
#         return [min(b[0], u), max(b[1], u), min(b[2], v), max(b[3], v)]


class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        inf = 10000000
        points = list(set([(x, y) for x, y in points]))
        n = len(points)
        t = points[0]
        d = [self.d(p, t) for p in points]
        c = [1] + [0] * (n - 1)
        dis = 0
        while 0 in c:
            t = [a + b * inf for a, b in zip(d, c)]
            m = min(t)
            dis += m
            t = t.index(m)
            c[t] = 1
            t = points[t]
            d = [min(d[i], self.d(p, t)) for i, p in enumerate(points)]
        return dis

    def d(self, p, q):
        return abs(p[0] - q[0]) + abs(p[1] - q[1])


if __name__ == '__main__':
    solution = Solution()
    print(solution.minCostConnectPoints(points=[[0,0],[2,2],[3,10],[5,2],[7,0]]))
    print(solution.minCostConnectPoints(points=[[3,12],[-2,5],[-4,1]]))
    print(solution.minCostConnectPoints(points=[[11,-6],[9,-19],[16,-13],[4,-9],[20,4],[20,7],[-9,18],[10,-15],[-15,3],[6,6]]))
