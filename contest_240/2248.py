from typing import List


class Solution:

    def intersection(self, nums: List[List[int]]) -> List[int]:
        prev = set(nums[0])
        for num in nums[1:]:
            cur = set()
            for n in num:
                if n in prev:
                    cur.add(n)
            prev = cur
        prev = list(prev)
        prev.sort()
        return prev


if __name__ == '__main__':
    solution = Solution()
    print(solution.intersection(nums=[[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
    print(solution.intersection(nums=[[1,2,3],[4,5,6]]))
