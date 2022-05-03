from typing import List


class Solution:

    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = []; b = []
        for num in nums:
            if num % 2 == 0:
                a.append(num)
            else:
                b.append(num)
        return a + b


if __name__ == '__main__':
    solution = Solution()
    print(solution.sortArrayByParity(nums=[3,1,2,4]))
    print(solution.sortArrayByParity(nums=[0]))
