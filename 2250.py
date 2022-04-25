from typing import List


class Solution:

    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        d = {}
        for x, y in rectangles:
            if y in d:
                d[y].append(x)
            else:
                d[y] = [x]
        for y in d:
            d[y].sort()
        k = list(d.keys())
        k.sort()
        l = []
        for x, y in points:
            a = 0
            for y in k[self.bs(k, y):]:
                a += len(d[y]) - self.bs(d[y], x)
            l.append(a)
        return l

    def bs(self, a, x):
        l = 0; r = len(a)
        while l + 1 < r:
            m = (l + r) // 2
            if a[m] < x:
                l = m
            elif a[m] > x:
                r = m
            else: return m
        if x <= a[l]: return l
        return r

    # def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
    #     l = []
    #     for point in points:
    #         a = 0
    #         for rectangle in rectangles:
    #             if self.check(point, rectangle):
    #                 a += 1
    #         l.append(a)
    #     return l

    # def check(self, a, b):
    #     if a[0] <= b[0] and a[1] <= b[1]: return True
    #     return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.countRectangles(rectangles=[[1,2],[2,3],[2,5]], points=[[2,1],[1,4]]))
    print(solution.countRectangles(rectangles=[[1,1],[2,2],[3,3]], points=[[1,3],[1,1]]))
