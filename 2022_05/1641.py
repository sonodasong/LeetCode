class Solution:

    def countVowelStrings(self, n: int) -> int:
        d = {}
        return self.find(n, 0, d)

    def find(self, n, i, d):
        if n == 1: return 5 - i
        if (n, i) in d: return d[(n, i)]
        a = 0
        for x in range(i, 5):
            a += self.find(n - 1, x, d)
        d[(n, i)] = a
        return a


if __name__ == '__main__':
    solution = Solution()
    print(solution.countVowelStrings(n=1))
    print(solution.countVowelStrings(n=2))
    print(solution.countVowelStrings(n=33))
