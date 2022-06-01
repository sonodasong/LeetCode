class Solution:

    def hasAllCodes(self, s: str, k: int) -> bool:
        n = len(s)
        h = 2 ** k
        if n - k + 1 < h: return False
        a = set()
        for i in range(n - k + 1):
            t = s[i:i + k]
            if t not in a:
                a.add(t)
            if len(a) == h: return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.hasAllCodes(s='00110110', k=2))
