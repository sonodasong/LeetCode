from typing import List
from bisect import bisect_left


class Solution:

    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        a = self.find(height, n)
        height.reverse()
        b = self.find(height, n)
        l = []
        for k in a:
            l.append(k * (n - 1 - b[k] - a[k]))
        return max(l)

    def find(self, height, n):
        a = {}
        b = []
        for h in height:
            if h in a: continue
            a[h] = None
            b.append(h)
        b.sort()
        i = 0
        while len(b) > 0:
            if height[i] >= b[0]:
                j = bisect_left(b, height[i])
                for k in b[:j + 1]:
                    a[k] = i
                b = b[j + 1:]
            i += 1
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxArea(height=[1,8,6,2,5,4,8,3,7]))
    print(solution.maxArea(height=[1,1]))
    print(solution.maxArea(height=[1,2]))
