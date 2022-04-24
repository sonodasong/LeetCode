class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        x = str(x); n = len(x)
        for i in range(n // 2):
            if not x[i] == x[n - i - 1]: return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPalindrome(x=121))
