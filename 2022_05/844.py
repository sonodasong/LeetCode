class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.c(s) == self.c(t)

    def c(self, s):
        l = []
        for c in s:
            if c == '#':
                if len(l) > 0:
                    l.pop()
            else:
                l.append(c)
        return ''.join(l)


if __name__ == '__main__':
    solution = Solution()
    print(solution.backspaceCompare(s='ab#c', t='ad#c'))
    print(solution.backspaceCompare(s='ab##', t='c#d#'))
    print(solution.backspaceCompare(s='a#c', t='b'))
    print(solution.backspaceCompare(s='y#fo##f', t='y#f#o##f'))
