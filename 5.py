class Solution:

    def longestPalindrome(self, s: str) -> str:
        m = 1; p = s[0]
        n = len(s)
        for i in range(n):
            f = -1
            for j in range(1, min(i + 1, n - i)):
                if not s[i - j] == s[i + j]:
                    f = -1
                    if j * 2 - 1 > m:
                        m = j * 2 - 1
                        p = s[i - j + 1:i + j]
                    break
                f = j
            if f > 0 and f * 2 + 1 > m:
                m = f * 2 + 1
                p = s[i - f:i + f + 1]
        for i in range(n - 1):
            f = -1
            for j in range(1, min(i + 2, n - i)):
                if not s[i - j + 1] == s[i + j]:
                    f = -1
                    if j * 2 - 2 > m:
                        m = j * 2 - 2
                        p = s[i - j + 2:i + j]
                    break
                f = j
            if f > 0 and f * 2 > m:
                m = f * 2
                p = s[i - f + 1:i + f + 1]
        return p


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestPalindrome(s='babad'))
    print(solution.longestPalindrome(s='cbbd'))
