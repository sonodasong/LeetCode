from typing import List


class Solution:

    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        i = 0
        while i + 1 < n and nums[i] >= nums[i + 1]:
            i += 1
        if i + 2 >= n: return False
        l = []
        a = nums[i]; b = nums[i + 1]
        for x in nums[i + 2:]:
            if b is None:
                if x <= a:
                    a = x
                elif len(l) > 0 and l[-1][0] < x and x < l[-1][1]: return True
                else:
                    l, t = self.reduce(l, x)
                    if t: return True
                    b = x
            else:
                if x > b:
                    l, t = self.reduce(l, x)
                    if t: return True
                    b = x
                elif x < a:
                    l.append((a, b))
                    a = x; b = None
                elif a < x and x < b: return True
        return False

    def reduce(self, l, b):
        while len(l) > 0:
            if b <= l[-1][0]: break
            if b >= l[-1][1]: del l[-1]; continue
            return l, True
        return l, False


if __name__ == '__main__':
    solution = Solution()
    print(solution.find132pattern(nums=[1,2,3,4]))
    print(solution.find132pattern(nums=[3,1,4,2]))
    print(solution.find132pattern(nums=[-1,3,2,0]))
    print(solution.find132pattern(nums=[3,5,0,3,4]))
    print(solution.find132pattern(nums=[10,12,6,8,3,11]))
