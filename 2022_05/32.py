from typing import List


class Solution:

    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n <= 1: return 0
        l = []
        for i in range(1, len(s)):
            if s[i] == '(': continue
            if len(l) > 0 and l[-1][1] == i - 1:
                if l[-1][0] > 0 and s[l[-1][0] - 1] == '(':
                    l[-1][0] -= 1
                    l[-1][1] += 1
                    if len(l) > 1 and l[-2][1] + 1 == l[-1][0]:
                        l[-2][1] = l[-1][1]
                        del l[-1]
            elif s[i - 1] == '(':
                if len(l) > 0 and l[-1][1] == i - 2:
                    l[-1][1] = i
                else:
                    l.append([i - 1, i])
        return 0 if len(l) == 0 else max([b - a + 1 for a, b in l])


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestValidParentheses(s='(()'))
    print(solution.longestValidParentheses(s=')()())'))
