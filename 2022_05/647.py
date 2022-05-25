class Solution:

    def countSubstrings(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            c += len(self.kmp(s[i:])) - 1
        return c

    def kmp(self, s):
        n = len(s)
        if n < 2: return set(list(range(n + 1)))
        r = set()
        b = self.build(s, n)
        i = n - 1; j = 0; l = i + 1
        while i >= 0:
            if s[i] == s[j]:
                if j >= l // 2 - 1:
                    r.add(l)
                    j = b[j]
                    if l == i + j + 1: break
                    l = i + j + 1
                else:
                    i -= 1
                    j += 1
            elif j == 0:
                i -= 1
                l = i + 1
            else:
                j = b[j]
                l = i + j + 1
        if s[0] == s[1]:
            r.add(2)
        r.add(1); r.add(0)
        return r

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
    print(solution.countSubstrings(s='abc'))
    print(solution.countSubstrings(s='aaa'))
