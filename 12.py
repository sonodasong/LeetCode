class Solution:

    def intToRoman(self, num: int) -> str:
        n = [num % (i * 10) // i for i in [1000, 100, 10, 1]]
        return self.d3(n[0]) + self.d2(n[1]) + self.d1(n[2]) + self.d0(n[3])

    def d3(self, n):
        if n == 0: return ''
        return 'M' * n

    def d2(self, n):
        if n == 0: return ''
        if n == 9: return 'CM'
        elif n == 4: return 'CD'
        elif n < 4: return 'C' * n
        else: return 'D' + 'C' * (n - 5)

    def d1(self, n):
        if n == 0: return ''
        if n == 9: return 'XC'
        elif n == 4: return 'XL'
        elif n < 4: return 'X' * n
        else: return 'L' + 'X' * (n - 5)

    def d0(self, n):
        if n == 0: return ''
        if n == 9: return 'IX'
        elif n == 4: return 'IV'
        elif n < 4: return 'I' * n
        else: return 'V' + 'I' * (n - 5)


if __name__ == '__main__':
    solution = Solution()
    print(solution.intToRoman(num=3))
    print(solution.intToRoman(num=58))
    print(solution.intToRoman(num=1994))
