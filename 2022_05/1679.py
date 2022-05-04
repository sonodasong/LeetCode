from typing import List


class Solution:

    def maxOperations(self, nums: List[int], k: int) -> int:
        a = {}
        b = 0
        for x in nums:
            t = k - x
            if t in a and a[t] > 0:
                a[t] -= 1
                b += 1
            elif x in a:
                a[x] += 1
            else:
                a[x] = 1
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxOperations(nums=[1,2,3,4], k=5))
    print(solution.maxOperations(nums=[3,1,3,4,3], k=6))
    print(solution.maxOperations(nums=[2,5,4,4,1,3,4,4,1,4,4,1,2,1,2,2,3,2,4,2], k=3))
