class Solution:

    def removeDuplicates(self, s: str, k: int) -> str:
        l = []
        a = None; b = 0
        for c in s:
            if c == a:
                b += 1
            else:
                l.append((a, b))
                a = c; b = 1
        l.append((a, b))
        t = [[None, 0]]
        for c, n in l[1:]:
            a, b = t[-1]
            n %= k
            if a == c:
                b = (b + n) % k
                if b == 0:
                    del t[-1]
                else:
                    t[-1][1] = b
            elif n > 0:
                t.append([c, n])
        r = ''
        for c, n in t[1:]:
            r += c * n
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.removeDuplicates(s='abcd', k=2))
    print(solution.removeDuplicates(s='deeedbbcccbdaa', k=3))
    print(solution.removeDuplicates(s='pbbcggttciiippooaais', k=2))
