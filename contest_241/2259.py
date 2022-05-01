class Solution:

    def countPrefixes(self, number: str, digit: str) -> str:
        l = [i for i, n in enumerate(number) if n == digit]
        return str(max([int(number[:i] + number[i + 1:]) for i in l]))


if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrefixes(number='123', digit='3'))
    print(solution.countPrefixes(number='1231', digit='1'))
    print(solution.countPrefixes(number='551', digit='5'))
