from typing import List


class Solution:

    def maxProduct(self, words: List[str]) -> int:
        d = {}
        for i, c in enumerate('abcdefghijklmnopqrstuvwxyz'):
            d[c] = i
        l = [self.c(d, word) for word in words]
        w = [len(word) for word in words]
        n = len(l)
        a = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.check(l[i], l[j]):
                    t = w[i] * w[j]
                    if t > a:
                        a = t
        return a

    def c(self, d, word):
        r = [False] * 26
        for c in word:
            r[d[c]] = True
        return r

    def check(self, a, b):
        for x, y in zip(a, b):
            if x and y: return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.maxProduct(words=['abcw','baz','foo','bar','xtfn','abcdef']))
    print(solution.maxProduct(words=['a','ab','abc','d','cd','bcd','abcd']))
    print(solution.maxProduct(words=['a','aa','aaa','aaaa']))
