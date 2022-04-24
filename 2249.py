from typing import List
from math import sqrt


class Solution:

    def countLatticePoints(self, circles: List[List[int]]) -> int:
        circles = [self.check_one(circle) for circle in circles]
        a = set(circles[0])
        for circle in circles:
            for c in circle:
                if not c in a:
                    a.add(c)
        return len(a)

    def check_one(self, circle):
        x, y, r = circle
        r2 = r ** 2
        l = []
        for i in range(-r, r + 1):
            a = int(sqrt(r ** 2 - i ** 2))
            for j in range(-a, a + 1):
                l.append((x + j, y + i))
        return l


if __name__ == '__main__':
    solution = Solution()
    print(solution.countLatticePoints(circles=[[2,2,1]]))
    print(solution.countLatticePoints(circles=[[2,2,2],[3,4,1]]))
