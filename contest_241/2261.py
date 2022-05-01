from typing import List
from bisect import bisect_right


class Solution:

    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        a = set()
        l = [i for i, n in enumerate(nums) if n % p == 0]
        for i in range(len(nums)):
            self.find(nums, a, l, k, i)
        return len(a)

    def find(self, nums, a, l, k, i):
        t = bisect_right(l, i)
        if t > k:
            self.add(nums, a, l[t - k - 1] + 1, i)
        else:
            self.add(nums, a, 0, i)

    def add(self, nums, a, x, y):
        for i in range(x, y + 1):
            a.add(tuple(nums[k] for k in range(i, y + 1)))



if __name__ == '__main__':
    solution = Solution()
    print(solution.countDistinct(nums=[2,3,3,2,2], k=2, p=2))
    print(solution.countDistinct(nums=[1,2,3,4], k=4, p=1))
