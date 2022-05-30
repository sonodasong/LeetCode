class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        a = 1
        if divisor < 0:
            divisor *= -1
            a *= -1
        if dividend < 0:
            dividend *= -1
            a *= -1
        r = int(dividend // divisor) * a
        if r > 2147483647:
            r = 2147483647
        elif r < -2147483648:
            r = -2147483648
        return r


if __name__ == '__main__':
    solution = Solution()
    print(solution.divide(dividend=10, divisor=3))
    print(solution.divide(dividend=7, divisor=-3))
