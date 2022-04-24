class Solution:

    def myAtoi(self, s: str) -> int:
        a = []; p = True
        state = False
        s = s.strip()
        for s in s:
            if state:
                if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    a.append(s)
                else: break
            else:
                if s in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    a.append(s)
                    state = True
                elif s == '-':
                    p = False
                    state = True
                elif s == '+':
                    state = True
                else: return 0
        a = self.remove(a)
        t = self.check(a, p)
        a = a if t is None else t
        s = 0
        for a in a:
            s *= 10
            s += a
        if not p: return - s
        return s

    def remove(self, a):
        i = 0
        for d in a:
            if d == '0':
                i += 1
            else: break
        return [int(a) for a in a[i:]]

    def check(self, a, p):
        p = [2, 1, 4, 7, 4, 8, 3, 6, 4, 7] if p else [2, 1, 4, 7, 4, 8, 3, 6, 4, 8]
        n = len(a)
        if n > 10: return p
        a = [0] * (10 - n) + a
        for a, pp in zip(a, p):
            if a < pp: return None
            if a == pp: continue
            return p
        return None


if __name__ == '__main__':
    solution = Solution()
    print(solution.myAtoi(s='4193 with words'))
    print(solution.myAtoi(s='words and 987'))
    print(solution.myAtoi(s='-91283472332'))
    print(solution.myAtoi(s='21474836460'))
