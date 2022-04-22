class Solution:

    def reverse(self, x: int) -> int:
        a = []
        if x < 0: p = False; x = - x
        else: p = True
        while x > 0:
            a.append(x % 10)
            x //= 10
        if not self.check(a, p): return 0
        s = 0
        for a in a:
            s *= 10
            s += a
        if not p: return - s
        return s

    def check(self, a, p):
        p = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7] if p else [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        a = [0] * (10 - len(a)) + a
        for a, p in zip(a, p):
            if a < p: return True
            if a == p: continue
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverse(x=123))
