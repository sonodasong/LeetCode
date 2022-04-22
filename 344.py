from typing import List


class Solution:

    def reverseString(self, s: List[str]) -> None:
        n = len(s)
        for i in range(n // 2):
            t = s[i]
            s[i] = s[n - i - 1]
            s[n - i - 1] = t


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseString(s=['h','e','l','l','o']))
