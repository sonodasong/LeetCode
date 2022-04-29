from typing import List


class Solution:

    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        r_words = [w[::-1] for w in words]
        r_dict = {w:i for i, w in enumerate(r_words)}
        t = [[self.kmp(w), self.kmp(rw)] for w, rw in zip(words, r_words)]
        l = set()
        for i, w in enumerate(words):
            f, r = t[i]
            for f in f:
                a = w[f:]
                if a in r_dict:
                    a = r_dict[a]
                    if not a == i:
                        l.add((a, i))
            n = len(w)
            for r in r:
                a = w[:n-r]
                if a in r_dict:
                    a = r_dict[a]
                    if not a == i:
                        l.add((i, a))
        return [[x, y] for x, y in l]

    def check(self, words, r_words, t, i, j):
        wi = words[i]; wj = r_words[j]
        ni = len(wi); nj = len(wj)
        _, r = t[i]
        if ni - nj in r and wi[:nj] == wj: return True

        wi = r_words[i]; wj = words[j]
        ni = len(wi); nj = len(wj)
        f, _ = t[j]
        if nj - ni in f and wj[nj - ni:] == wi: return True
        return False

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
    print(solution.palindromePairs(words=['abcd','dcba','lls','s','sssll']))
    print(solution.palindromePairs(words=['bat','tab','cat']))
    print(solution.palindromePairs(words=['a','']))
    print(solution.palindromePairs(words=['a','abc','aba','']))
    print(solution.palindromePairs(words=['a','aa','aaa']))
