class Solution:

    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        n = len(s); p = numRows * 2 - 2
        d = {}
        for i in range(numRows):
            d[i] = ''
        for i, c in enumerate(s):
            d[self.f(i, numRows, p)] += c
        s = ''
        for i in range(numRows):
            s += d[i]
        return s

    def f(self, i, r, p):
        a = i // p
        i %= p
        # if i < r: return (i, (r - 1) * a)
        # return (p - i, (r - 1) * (a - 1) + i)
        if i < r: return i
        return p - i


if __name__ == '__main__':
    solution = Solution()
    print(solution.convert(s='PAYPALISHIRING', numRows=1))
