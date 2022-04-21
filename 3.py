class Solution:

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     n = len(s); m = 0
    #     if n == 0: return m
    #     d = {}
    #     i = 0; j = 0
    #     while j < n:
    #         c = s[j]
    #         if self.check(d, c):
    #             d[s[i]] = False
    #             i += 1
    #         else:
    #             j += 1
    #             if j - i > m:
    #                 m = j - i
    #             d[c] = True
    #     return m

    # def check(self, d, k):
    #     if k in d: return d[k]
    #     return False

    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s); m = 0
        if n == 0: return m
        d = {}
        i = 0; j = 0
        while j < n:
            c = s[j]
            t = self.check(d, c)
            if t >= i:
                i = t + 1
            else:
                d[c] = j
                j += 1
                if j - i > m:
                    m = j - i
        return m

    def check(self, d, k):
        if k in d: return d[k]
        return -1


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring(s='abcabcbb'))
    print(solution.lengthOfLongestSubstring(s='bbbbb'))
    print(solution.lengthOfLongestSubstring(s='pwwkew'))
