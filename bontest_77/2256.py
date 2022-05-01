from typing import List


class Solution:

    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        a = [nums[0]]
        for i in nums[1:]:
            a.append(a[-1] + i)
        nums.reverse()
        b = [nums[0]]
        for i in nums[1:]:
            b.append(b[-1] + i)
        b.reverse()
        l = [abs(a[i] // (i + 1) - b[i + 1] // (n - i - 1)) for i in range(n - 1)]
        l.append(a[-1] // n)
        return l.index(min(l))


if __name__ == '__main__':
    solution = Solution()
    print(solution.minimumAverageDifference(nums=[2,5,3,9,5,3]))
    print(solution.minimumAverageDifference(nums=[0]))
