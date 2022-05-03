from typing import List
from bisect import bisect_right


class Solution:

    def findUnsortedSubarray(self, nums: List[int]) -> int:
        a = None; b = None; m = None
        for i in range(1, len(nums)):
            x = nums[i]
            if m is None and x < nums[i - 1]:
                a = bisect_right(nums[:i], x)
                b = i
                m = max(x, nums[i - 1])
            elif m is not None and x < max(m, nums[i - 1]):
                if x < nums[a - 1]:
                    a = bisect_right(nums[:a], x)
                b = i
                m = max(m, nums[i - 1])
        if m is None: return 0
        return b - a + 1


if __name__ == '__main__':
    solution = Solution()
    print(solution.findUnsortedSubarray(nums=[2,6,4,8,10,9,15]))
    print(solution.findUnsortedSubarray(nums=[1,2,3,4]))
    print(solution.findUnsortedSubarray(nums=[1]))
