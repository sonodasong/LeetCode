class Solution:

    def isMatch(self, s: str, p: str) -> bool:
        s = '^' + s + '#'
        p = self.p_pass_1(p)
        p = self.p_pass_2(p)
        n = len(p[0][1])
        if not s[:n] == p[0][1]: return False
        return self.match_1(s[n:], p[1:])

    def match_1(self, s, p):
        if len(s) == 0 and len(p) == 0: return True
        p1, p2 = p[0]
        l = self.kmp(s, p2)
        if len(l) == 0: return False
        for b, e in l:
            if not self.match_2(s[:b], p1): continue
            if self.match_1(s[e:], p[1:]): return True
        return False

    def match_2(self, s, p, peak=None):
        ns = len(s)
        if ns == 0:
            for c, x in p:
                if not x == 0: return False
            return True
        if len(p) == 0: return False
        pc, px = p[0]
        if pc == '.':
            if px < 0:
                if px + ns < 0: return False
                return self.match_2(s[-px:], p[1:])
            else:
                if px > ns: return False
                for i in range(px, ns + 1):
                    if self.match_2(s[i:], p[1:]): return True
                return False
        elif pc == s[0]:
            n = self.peak(s) if peak is None or peak == 0 else peak
            if px > n: return False
            for i in range(px, n + 1):
                if self.match_2(s[i:], p[1:], n - i): return True
            return False
        else:
            if px == 0: return self.match_2(s, p[1:])
            return False

    def peak(self, s):
        c = s[0]; a = 1
        for s in s[1:]:
            if not s == c: break
            a += 1
        return a

    def p_pass_1(self, p):
        l = []
        prev = '^'; count = -1
        for c in p + '#':
            if c == prev:
                count += -1 if count < 0 else 1
            elif c == '*':
                count = abs(count) - 1
            else:
                l.append((prev, count))
                prev = c; count = -1
        return l + [('#', -1)]

    def p_pass_2(self, p):
        l = []; f = True
        l1 = []; l2 = ''
        for c, x in p:
            if f:
                if x < 0 and c != '.':
                    l2 += c * (-x)
                else:
                    l.append((l1, l2))
                    l1 = []; l2 = ''
                    l1.append((c, x))
                    f = False
            else:
                if x < 0 and c != '.':
                    l2 += c * (-x)
                    f = True
                else:
                    l1.append((c, x))
        l.append((l1, l2))
        return l

    def kmp(self, s, p):
        b = self.build(p)
        l = []
        i = 0; j = 0
        n = len(p)
        while i < len(s):
            if j == n:
                l.append((i - n, i))
                j = b[j]
            elif s[i] == p[j]:
                i += 1
                j += 1
            elif j == 0:
                i += 1
            else:
                j = b[j]
        if j == n:
            l.append((i - n, i))
        return l

    def build(self, p):
        i = 1; j = 0
        b = [j]
        while i < len(p):
            if len(b) == i:
                b.append(j)
            if p[i] == p[j]:
                i += 1; j += 1
            elif j == 0:
                i += 1
            else:
                j = 0
        b.append(j)
        return b


if __name__ == '__main__':
    solution = Solution()
    print(solution.isMatch(s='acababac', p='.*aba.*'))
    print(solution.isMatch(s='bbab', p='b*a*.b*'))
    print(solution.isMatch(s='aa', p='a'))
    print(solution.isMatch(s='ab', p='.*'))
