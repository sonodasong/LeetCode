from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, a in enumerate(nums):
            t = target - a
            n = nums[i + 1:]
            if t in n: return [i, n.index(t) + i + 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.twoSum(nums=[2, 7, 11, 15], target=9))
