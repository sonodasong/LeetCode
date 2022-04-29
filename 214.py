class Solution:

    # def shortestPalindrome(self, s: str) -> str:
    #     n = len(s)
    #     if n < 2: return s
    #     for i in range(n):
    #         i = n - i
    #         if self.check(s[:i]):
    #             m = i
    #             break
    #     return s[m:][::-1] + s

    # def check(self, s):
    #     n = len(s) // 2
    #     if n == 0: return True
    #     return s[:n][::-1] == s[-n:]

    def shortestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2: return s
        b = self.build(s, n)
        i = n - 1; j = 0; l = i + 1
        while True:
            if s[i] == s[j]:
                if j >= l // 2 - 1: break
                i -= 1
                j += 1
            elif j == 0:
                i -= 1
                l = i + 1
            else:
                j = b[j]
                l = i + j + 1
        return s[l:][::-1] + s

    def build(self, s, n):
        i = 1; j = 0
        b = [j]
        while i < n:
            if len(b) == i:
                b.append(j)
            if s[i] == s[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = 0
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.shortestPalindrome(s='aacecaaa'))
    print(solution.shortestPalindrome(s='abcd'))
    print(solution.shortestPalindrome(s='babbbabbaba'))
