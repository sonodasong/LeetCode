class Solution:

    def hammingWeight(self, n: int) -> int:
        return sum([1 for i in range(32) if (1 << i) & n])


if __name__ == '__main__':
    solution = Solution()
    print(solution.hammingWeight(n=11))
